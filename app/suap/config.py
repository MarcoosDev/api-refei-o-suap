import os
from dotenv import load_dotenv

load_dotenv()

class SuapConfig:
    URL = "https://suap.ifpi.edu.br/"
    CLASSNAME_CARD_REFEICOES = "card"

    MATRICULA = os.getenv("MATRICULA")
    SENHA = os.getenv("SENHA")