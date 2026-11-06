from app.services.suap import Suap

suap = Suap()
suap.acessar_pagina()
elemento = suap.buscar_elemento_por_class_name(valule = "card")
print(elemento.text)

suap.fechar()