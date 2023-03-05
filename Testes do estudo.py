# Fazendo uma contagem de while

x = 0 
while x <= 10:
    y = 0 
    while y <= 5:
        print(f'X vale {x} e Y vale {y} ')
        y = y + 1

    x = x + 1

# Calculadora simples

while True:
    print()
    print('Se deseja sair do programa, digite SAIR em num1, ou num2')
    num1 = input('Digite um número: ')
    num2 = input('Digite um número: ')
    operad = input('Digite um operador: ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar algo!')
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operad == '+':
        print(num1 + num2)
    if operad == '-':
        print(num1 - num2)
    if operad == '/':
        print(num1 / num2)
    if operad == '*':
        print(num1 * num2)    

    elif num1 or num2 == 'SAIR':
        break
    

