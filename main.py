from SUAP import SUAP

suap = SUAP()
elemento = suap.buscar_elemento_por_class_name(valule = "card")
print(elemento.text)