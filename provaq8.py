def ocultar(texto: str, visiveis: int =2, simbolo: str = "*") -> str:
    if len(texto) <= visiveis:
        return texto
    parte1 = texto[:visiveis]
    parte2 = simbolo * (len(texto) - visiveis)
    return parte1 + parte2

print(ocultar("senha123"))
print(ocultar(texto = "abc", visiveis = 4, simbolo = "#"))
print(ocultar(texto = "Python", simbolo = "-"))