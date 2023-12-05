from bs4 import BeautifulSoup
from selenium import webdriver
import json

class ozon_parsing():
    def __init__(self, url:str):
        self.url = url
        self.driver = webdriver.Chrome()

    def get_info(self, url:str):
        self.src = self.driver.get(url)
        self.srcdata = self.driver.page_source
        self.soup = BeautifulSoup(self.srcdata, 'html.parser').find('span', attrs={'class': {'lm7 l5m','ml3 m1l'}})
        return str(self.soup.get_text())