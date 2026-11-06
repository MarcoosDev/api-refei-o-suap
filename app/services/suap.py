from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from typing import List
from app.suap.config import SuapConfig
from app.schemas.refeicoes_schema import Refeicao

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
    
    def buscar_todas_refeicoes(self) -> List[WebElement]:
        return self.__driver.find_elements(By.CLASS_NAME, SuapConfig.CLASSNAME_CARD_REFEICOES)

    def buscar_refeicao(self, refeicao : Refeicao) -> WebElement:
        ref = self.__driver.find_elements(By.CLASS_NAME, SuapConfig.CLASSNAME_CARD_REFEICOES)[refeicao]
        return ref

    def save_screenshot(self, filename: str) -> WebDriver:
        return self.__driver.save_screenshot(filename)
        