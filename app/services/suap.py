from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from typing import List
from app.suap.config import SuapConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.schemas.refeicoes_schema import Refeicao
from app.suap.config import SuapConfig

class Suap:
    URL = SuapConfig.URL

    def __init__(self):
        self.__driver = self.__create_driver()
        self.espera = WebDriverWait(self.__driver, 15)


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
        return self.__driver.find_elements(By.CLASS_NAME, SuapConfig.CLASSNAME_CARD_REFEICOES)[refeicao]


    def login(self):
        user = self.espera.until(EC.visibility_of_element_located((By.ID, "id_username")))
        user.send_keys(SuapConfig.MATRICULA)

        senha = self.__driver.find_element(By.ID, "id_password")
        senha.send_keys(SuapConfig.SENHA)

        comfirmar = self.espera.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.success")))
        comfirmar.click()


    def acessar_painel_de_refeicoes(self):
        child_atividades_estudantis = self.espera.until(EC.element_to_be_clickable((By.CLASS_NAME, "has-child.menu-atividades-estudantis")))
        child_atividades_estudantis.click()
        restaurante_institucional = self.espera.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='Restaurante Institucional']")))
        restaurante_institucional.click()
        reservar_ref = self.espera.until(EC.element_to_be_clickable((By.ID, "menu-item-atividadesestudantis_restauranteinstitucional_reservarrefeições")))
        reservar_ref.click()


    def save_screenshot(self, filename: str) -> WebDriver:
        return self.__driver.save_screenshot(filename)