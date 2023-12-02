from bs4 import BeautifulSoup
from selenium import webdriver

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

    def get_json(self, url:str):
        self.src = self.driver.get(url)
        self.srcdata = self.driver.page_source
        self.soup = BeautifulSoup(self.srcdata, 'html.parser')
        self.result = self.soup.findAll('span')
        self.captured_data = []
        for self.data in self.result:
            if self.data.find('span', class_="15m m13") is not None:
                self.captured_data.append(self.data)
        if self.captured_data == []:
            return "None"