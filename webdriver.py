from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from sys import platform
import pickle

def create_webdriver(headless=False):
    if platform == "linux" or platform == "linux2":
        if headless:
            from pyvirtualdisplay import Display
            display = Display(visible=0, size=(1024, 768))
            display.start()
        driver = webdriver.Firefox()
    else:
        options = Options()
        options.headless = headless
        driver = webdriver.Firefox(options=options)
    return driver
