def analisar(texto : str, letra: str = "a") -> str:
    cont = 0
    i = 0

    while i < len(texto):
        if texto[i].lower() == letra:
            cont = cont +1
        i +=2

    if cont == 0:
        return "nenhuma"
    elif cont <= 2:
        return "poucas"
    else:
        return "muitas"
print(analisar("Abacate", letra ="a"))
print(analisar(texto = "banana"))