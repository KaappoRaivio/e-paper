
import epd4in2b
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class Drawer:
    def __enter__(self):
        self.epd = epd4in2b.EPD()
        self.epd.init()
        return self

    def draw(self, black, red):
        try:
            frame_black = self.epd.get_frame_buffer(black)
            frame_red = self.epd.get_frame_buffer(red)
            self.epd.display_frame(frame_black, frame_red)
        except NameError:
            raise Exception("Must be used through context manager")

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# def main():
#
#
# if __name__ == '__main__':
#     main()
