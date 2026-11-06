from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from typing import List
from app.suap.config import SuapConfig

class Suap:
    URL = SuapConfig.URL
    
    def __init__(self):
        self.__driver = self.__create_driver()

    def __create_driver(self) -> webdriver.Chrome:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        return webdriver.Chrome(options=options)

    def acessar_pagina(self) -> None:
        self.__driver.get(self.URL)

    def fechar(self) -> None:
        self.__driver.quit()

    def buscar_elemento_por_class_name(self, valule : str) -> WebElement:
        return self.__driver.find_element(By.CLASS_NAME, valule)
    
    def buscar_elementos_por_class_name(self, valule : str) -> List[WebElement]:
        return self.__driver.find_elements(By.CLASS_NAME, valule)

    def save_screenshot(self, filename: str) -> WebDriver:
        return self.__driver.save_screenshot(filename)
        