from app.services.suap import Suap
from app.schemas.refeicoes_schema import Refeicao

suap = Suap()
suap.acessar_pagina()
suap.login()
suap.acessar_painel_de_refeicoes()
suap.save_screenshot("screenshot.png")
oi = 3
oi = "sla"

suap.fechar()