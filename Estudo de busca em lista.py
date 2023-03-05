#
# O objetivo é analisar a lista de forma sequencial para procurar um elemento específico

def search(lista, elem):
    '''Retorna o índice do elemento se ele estiver na lista ou None caso contrário '''
    for i in range(len(lista)):
        if lista[i] == elem:
            return i 
        
    return None

listaes = [10, 30, 560, "python", "alegria", 40]
elemento = 40

indice = search(listaes, elemento)

if indice is not None:
    print(f'O indice de elemento {elemento} é {indice}')
else: 
    print(f'O elemento {elemento} não se encontra na lista')