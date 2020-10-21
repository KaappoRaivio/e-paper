import time

import converter
# from Drawer import Drawer
from screenshot import take_screenshot
import sys, os


def sleep_until_correct_time():
    time.sleep(15)


try:
    url = sys.argv[1]
except:
    url = "http://localhost:3000"

if __name__ == "__main__":
    # with Drawer() as drawer:
        while True:
            print("Taking screenshot")
            screenshot_path = take_screenshot(url)
            print("Converting")
            black, red = converter.convert(screenshot_path)
            print("Drawing")
            # drawer.draw(black, red)

            print("Sleeping")
            sleep_until_correct_time()


else:
    raise Exception("cannot be imported")