from selenium.webdriver.remote.webelement import WebElement
from app.suap.config import SuapConfig
from selenium.webdriver.common.by import By
from app.schemas.refeicoes_schema import Refeicao
from selenium import webdriver


class Services: 
 def __init__(self, driver: webdriver.Chrome):
   self._driver = driver

#def buscar_todas_refeicoes(self) -> List[WebElement]:
#    return self.__driver.find_elements(By.CLASS_NAME, SuapConfig.CLASSNAME_CARD_REFEICOES)


#def buscar_refeicao(self, refeicao : Refeicao) -> WebElement:
#    return self.__driver.find_elements(By.CLASS_NAME, SuapConfig.CLASSNAME_CARD_REFEICOES)[refeicao]

 #def ler_almoco (self, refeicao: Refeicao) -> WebElement:
   # almoco_do_dia = self._driver.find_elements(By.CLASS_NAME,'card').text
 #   print(almoco_do_dia.text)

 def ler_todas_as_refeicoes (self, refeicao: Refeicao) -> WebElement:
    almoco_do_dia = self._driver.find_elements(By.CLASS_NAME,'card').text
    for elements in almoco_do_dia:
     print(elements.text)


