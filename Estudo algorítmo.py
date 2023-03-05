list = [10, 20, 50, 60, 100]

def search_binary(list, target):
    left = 0 
    right = len(list) - 1
    middle = (left + right) // 2

    while(left <= right):
        middle = (left + right) // 2
        if list[middle] == target: 
            return middle 

        elif target > list[middle]:
            left = middle + 1

        elif target < list[middle]:
            right = middle - 1

    return -1

list = [10, 20, 50, 60, 100]
index = search_binary(list, 100)
if (index >= 0):
    print(f'Elemento encontrado na posição {index}!')

else: print('Valor não encontrado ')