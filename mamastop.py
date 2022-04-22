from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from bs4 import BeautifulSoup as bs

if os.getcwd() not in os.environ["PATH"]:
    os.environ["PATH"] += os.pathsep + os.getcwd()

driver = webdriver.Firefox()
driver.get("https://papago.naver.com/?sk=ko&tk=en&st=바보")
content = driver.page_source()
source = bs(content)