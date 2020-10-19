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
    im.thumbnail((400, 300))
    im = im.convert("RGB")

    p = Palette()

    data = np.array(im)   # "data" is a height x width x 4 numpy array
    print(data.shape)
    for y in range(data.shape[0]):
        for x in range(data.shape[1]):
            data[y, x] = p.getColor(data[y, x])

    # print(p.getColor(data[0, 0]))
    # red, green, blue, alpha = data.T # Temporarily unpack the bands for readability

    # Replace white with red... (leaves alpha values alone...)
    # white_areas = (red == 255) & (blue == 255) & (green == 255)
    # data[..., :-1][white_areas.T] = (0, 0, 255) # Transpose back needed
    #
    im2 = Image.fromarray(data)
    im2.save("temp.png")
    # im2.show()
    # im2.save("out.png", "png")
    out_red = channel(im2, 1)
    # out_black = np.array(im2) - out_red

    r = channel(im2, 0)
    g = channel(im2, 1)

    img_red = Image.fromarray(np.abs(r[:, :, 0]) - g[:, :, 1], "L")
    img_red = ImageOps.invert(img_red)
    img_red.convert("1")
    img_red.save("red.bmp")

    # img_black = Image.fromarray(black(im2), "L")
    threshold = 245
    # img_black = Image.fromarray(data)
    img_black = Image.fromarray(r[:, :, 0], "L")

    img_black = img_black.point(lambda p: 255 if p == 0 else 0)
    img_black.convert("1", dither=Image.NONE)
    img_black.save("black.bmp")


    a = Image.open("black.bmp")
    a = ImageOps.invert(a)
    a.save("black.bmp")

    # img_black.convert("1")



def black(img):
    data = np.array(img)   # "data" is a height x width x 4 numpy array
    red, green, blue = data.T # Temporarily unpack the bands for readability

    # Replace white with red... (leaves alpha values alone...)
    black_areas = (red == 0) & (blue == 0) & (green == 0)
    data[..., :-1][black_areas.T] = (255, 255, 255) # Transpose back needed

def channel(img, n):
    """Isolate the nth channel from the image.

       n = 0: red, 1: green, 2: blue
    """
    a = np.array(img)
    a[:,:,(n!=0, n!=1, n!=2)] *= 0
    return a


if __name__ == "__main__":
    convert()
    p = Palette()

    print(p.getColor((128, 128, 128)))