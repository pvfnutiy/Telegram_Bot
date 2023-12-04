from bs4 import BeautifulSoup
from selenium import webdriver
import json

class ozon_parsing():
    def __init__(self, url:str):
        self.url = url
        self.apiurl = "https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=%2F"
        self.rawurl = self.url.split('/')
        self.driver = webdriver.Chrome()

    def get_api_url(self):
        for i in range(0, 3):
            del self.rawurl[i]
        del self.rawurl[0]
        self.rawurl = '/'.join(self.rawurl)
        return self.apiurl + self.rawurl

    def get_info(self, url:str):
        self.src = self.driver.get(url)
        self.srcdata = self.driver.page_source
        self.result = BeautifulSoup(self.srcdata, 'html.parser').find("thinsp", class_="15m ml3")
        print(self.result)