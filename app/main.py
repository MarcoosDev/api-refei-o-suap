from app.suap.config import SuapConfig
from app.services.suap import Suap
from app.schemas.refeicoes_schema import Refeicao

suap = Suap()


suap.acessar_pagina()
suap.login()
suap.acessar_painel_de_refeicoes()
suap.save_screenshot("screenshot.png")
suap.suap_service.ler_todas_as_refeicoes(Refeicao.ALMOCO)
oi = 3
oi = "sla"

suap.fechar()