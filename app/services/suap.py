from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from app.suap.config import SuapConfig
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.suap.config import SuapConfig
from app.services.suap_services import Services

class Suap:
    URL = SuapConfig.URL

    def __init__(self):
        self.__driver = self.__create_driver()
        self.espera = WebDriverWait(self.__driver, 30)
        self.suap_service = Services(self.__driver)


    def __create_driver(self) -> webdriver.Chrome:
        options = Options()


        return webdriver.Chrome(options=options)


    def acessar_pagina(self) -> None:
        self.__driver.get(self.URL)


    def fechar(self) -> None:
        self.__driver.quit()

    

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

