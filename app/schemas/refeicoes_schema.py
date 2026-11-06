from pydantic import BaseModel
from enum import IntEnum
from selenium.webdriver.remote.webdriver import WebDriver

class Refeicao(IntEnum):
    ALMOCO = 0
    JANTAR = 1