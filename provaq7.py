def criar(nome: str, maiuscula : bool = True) -> str:
    partes = nome.split()
    sigla = ""
    for parte in partes:
        if len(parte)> 2:
            sigla += parte[0]
    if maiuscula:
        return sigla.upper()
    else:
        return sigla.lower()
    
print(criar("Instituto Federal do Ceará"))

    
