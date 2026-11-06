from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver

class Suap:
    URL = "https://suap.ifpi.edu.br/ae/refeicoes-publicas/?campus=6&filtracampus_form=CAPAR"

    def __init__(self):
        self._driver = webdriver.ChromiumEdge()

    def acessar_pagina(self) -> None:
        self._driver.get(self.URL)

    def fechar(self) -> None:
        self._driver.quit()

    def buscar_elemento_por_class_name(self, valule : str) -> WebElement:
        return self._driver.find_element(By.CLASS_NAME, valule)

    def save_screenshot(self, filename: str) -> WebDriver:
        return self._driver.save_screenshot(filename)
        