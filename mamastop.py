import urllib
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os
from os import listdir
import cv2
import easyocr as ocr
import ssl
from konlpy.tag import Mecab
import pyperclip

class MaMaStop:
    def __init__(self):
        self.dirpath = ""
        self.nouns = []
        self.reader = ocr.Reader(['ko'])
        self.mecab = Mecab()

    def process_dir(self, dirpath):
        self.dirpath = os.path.abspath(dirpath)
        fnames = [os.path.join(os.path.abspath(self.dirpath), x) for x in listdir(self.dirpath)]
        for fname in fnames:
            self.img_to_string(fname)

    def img_to_string(self, filepath):
        reader = ocr.Reader(['ko'])
        return " ".join(reader.readtext(filepath, detail = 0))

    def string_to_nouns(self, words):
        return self.mecab.nouns(words)

    def find_tl(self, input):
        if os.getcwd() not in os.environ["PATH"]:
            os.environ["PATH"] += os.pathsep + os.getcwd()

        pyperclip.copy(input)

        driver = webdriver.Firefox()
        driver.get("https://papago.naver.com/?sk=ko&tk=en&st=%EB%B0%94%EB%B3%B4")


