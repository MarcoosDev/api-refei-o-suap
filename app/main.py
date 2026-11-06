from app.services.suap import Suap
from app.schemas.refeicoes_schema import Refeicao

suap = Suap()
suap.acessar_pagina()
elemento = suap.buscar_refeicao(Refeicao.JANTAR)
print(elemento.text)

suap.fechar()