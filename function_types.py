def list_shift(lista, valor):
    for i in range(len(lista)):
        lista[i] = lista[i] + valor
def calc_avg(lista):
    suma = sum(lista)
    cantidad = len(lista)
    return suma / cantidad
def print_normalized(lista):
    print(lista)