from app.services.suap import Suap
from app.schemas.refeicoes_schema import Refeicao

suap = Suap()
suap.acessar_pagina()
elemento = suap.buscar_elementos_por_class_name(valule = "card")
print(elemento[Refeicao.JANTAR].text)

suap.fechar()