from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver

class SUAP:
    def __init__(self):
        self.url = "https://suap.ifpi.edu.br/ae/refeicoes-publicas/?campus=6&filtracampus_form=CAPAR"
        self.__driver = webdriver.ChromiumEdge()
        self.__driver.get(self.url)

    def buscar_elemento_por_class_name(self, valule : str) -> WebElement:
        return self.__driver.find_element(By.CLASS_NAME, valule)

    def save_screenshot(self, filename: str) -> WebDriver:
        return self.__driver.save_screenshot(filename)
        