import time

import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def take_screenshot(url):
    options = Options()
    options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(800, 600 + 74)
    driver.get(url)
    time.sleep(2)
    driver.save_screenshot("test.png")
    driver.close()

    return "test.png"

if __name__ == '__main__':
    take_screenshot("http://localhost:3000")