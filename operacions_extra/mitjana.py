def mitjana(llista):
    total = 0
    contador = 0
    for element in llista:
        total = total + element
        contador = contador + 1
     
    mitjana = total / contador
    return mitjana