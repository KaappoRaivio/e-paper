import math

import numpy as np
from PIL import Image, ImageOps
from PIL import ImageDraw

class Palette:
    def __init__(self):
        self.colors = [(255, 255, 255), (255, 0, 0), (0, 0, 0)]


    def getColor (self, c):
        diffs = {}
        for color in self.colors:
            diff = self.__abs(self.__subtract(color, c))
            diffs[diff] = color

        smallest = min(diffs)
        return np.array(diffs[smallest])

    @staticmethod
    def __subtract(a, b):
        # print(a, b)
        return [math.sqrt(abs(a[i] - b[i])) for i in range(3)]

    @staticmethod
    def __abs(a):
        return math.sqrt(a[0] ** 2 + a[1] ** 2 + a[2] ** 2)




def convert(file_path="test.png"):
    im = Image.open(file_path)
    # im.thumbnail((400, 300))
    im = im.crop((0, 0, 400, 300))
    im = im.convert("RGB")

    p = Palette()

    data = np.array(im)
    print(data.shape)
    for y in range(data.shape[0]):
        for x in range(data.shape[1]):
            data[y, x] = p.getColor(data[y, x])

    im2 = Image.fromarray(data)

    r = channel(im2, 0)
    g = channel(im2, 1)

    img_red = Image.fromarray(np.abs(r[:, :, 0]) - g[:, :, 1], "L")
    img_red = ImageOps.invert(img_red)
    img_red.convert("1")
    img_red.save("red.bmp")

    img_black = Image.fromarray(r[:, :, 0], "L")

    img_black = img_black.point(lambda p: 255 if p == 0 else 0)
    img_black.convert("1", dither=Image.NONE)
    img_black.save("black.bmp")


    a = Image.open("black.bmp")
    a = ImageOps.invert(a)
    a.save("black.bmp")

    return a, img_red



def black(img):
    data = np.array(img)
    red, green, blue = data.T

    black_areas = (red == 0) & (blue == 0) & (green == 0)
    data[..., :-1][black_areas.T] = (255, 255, 255)

def channel(img, n):
    a = np.array(img)
    a[:,:,(n!=0, n!=1, n!=2)] *= 0
    return a
