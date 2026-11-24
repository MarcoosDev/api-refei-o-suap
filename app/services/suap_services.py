from selenium.webdriver.remote.webelement import WebElement
from app.suap.config import SuapConfig
from selenium.webdriver.common.by import By
from app.schemas.refeicoes_schema import Refeicao
from selenium import webdriver


class Services: 
  def __init__(self, driver: webdriver.Chrome):
    self._driver : webdriver.Chrome = driver

  #def buscar_todas_refeicoes(self) -> List[WebElement]:
  #    return self.__driver.find_elements(By.CLASS_NAME, SuapConfig.CLASSNAME_CARD_REFEICOES)


  #def buscar_refeicao(self, refeicao : Refeicao) -> WebElement:
  #    return self.__driver.find_elements(By.CLASS_NAME, SuapConfig.CLASSNAME_CARD_REFEICOES)[refeicao]

  #def ler_almoco (self, refeicao: Refeicao) -> WebElement:
  # almoco_do_dia = self._driver.find_elements(By.CLASS_NAME,'card')
  #   print(almoco_do_dia.text)
  def print_refeicoes(self) -> any:
    refeicoes = self.ler_todas_as_refeicoes()

    """
    Almoço: Nome (00/00)
    Jantar: Nome (00/00)
    """
    pass

  def ler_todas_as_refeicoes (self, refeicao: Refeicao) -> list[WebElement]:
    refeicoes_do_dia = self._driver.find_elements(By.CLASS_NAME,'card')
    return refeicoes_do_dia






