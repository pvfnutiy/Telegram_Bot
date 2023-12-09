from bs4 import BeautifulSoup
from selenium import webdriver
import re

class ozon_parsing():
    def __init__(self, url:str):
        self.url = url
        self.driver = webdriver.Chrome()

    def get_info(self, url:str):
        self.Data = []
        self.src = self.driver.get(url)
        self.srcdata = self.driver.page_source
        self.soup = BeautifulSoup(self.srcdata, 'html.parser').findAll('div', attrs={'class': {'m4l'}})
        self.result = ''.join(str(self.soup[0]))
        self.result = re.split(">", self.result)

        for i in self.result:
            for j in i:
                if j == '₽':
                    self.Data.append(i)
        
        self.Data = ''.join(self.Data)
        self.Data = re.split("<"+"/span", self.Data)

        print(' '.join(self.Data))
        return f'Цена с озон-картой: {self.Data[0]}\nЦена без озон карты: {self.Data[1]}\nСтарая цена: {self.Data[2]}'