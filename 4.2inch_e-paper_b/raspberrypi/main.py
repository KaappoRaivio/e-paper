
import epd4in2b
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

COLORED = 1
UNCOLORED = 0

def main():
    epd = epd4in2b.EPD()
    epd.init()
    # For simplicity, the arguments are explicit numerical coordinates
    # image_red = Image.new('1', (epd4in2b.EPD_WIDTH, epd4in2b.EPD_HEIGHT), 255)    # 255: clear the frame
    # draw_red = ImageDraw.Draw(image_red)
    # image_black = Image.new('1', (epd4in2b.EPD_WIDTH, epd4in2b.EPD_HEIGHT), 255)    # 255: clear the frame
    # draw_black = ImageDraw.Draw(image_black)
    # font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 24)
    # draw_black.rectangle((0, 6, 400, 30), fill = 0)
    # draw_black.text((100, 10), 'e-Paper demo', font = font, fill = 255)
    # draw_black.arc((40, 80, 180, 220), 0, 360, fill = 0)
    # draw_red.rectangle((0, 0, 400, 300), fill = 0)
    # draw_red.arc((240, 80, 380, 220), 0, 360, fill = 255)

    # display the frames
    # epd.display_frame(epd.get_frame_buffer(image_black), epd.get_frame_buffer(image_red))

    # display images
    frame_black = epd.get_frame_buffer(Image.open('black.bmp'))
    frame_red = epd.get_frame_buffer(Image.open('red.bmp'))
    epd.display_frame(frame_black, frame_red)

if __name__ == '__main__':
    main()
