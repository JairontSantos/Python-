#Esse arquivo serve para estudo e anotações e para um projeto futuro 


#O print é uma ferramenta utilizado para que algo apareça no terminal
#Só é string algo que esteja dentro de '', ele será considerado uma string
#Mesmo sendo um número ou algo semelhante.

#Ex.
print('Jairon possui 18 anos e está estudando python!')

#Podemos usar o print também para fazer qualquer tipo de multiplicação
#e já obter o resultado

#Ex.
print(5+5)
print(5-5)
print(5*5)
print(5/5)

#Obs.: Podemos até transformar números em strings e somar eles com letras

#Ex.
print('5'+'B')

#Partindo para o lado dos cálculos podemos falar sobre os operações 
#Que em geral são:

# +  Soma
# -  Subtração
# *  Multiplicação
# /  Divisão
# // Divisão com resultado inteiro
# %  Modulo (resto da divisão)
# ** Potência

#Obs.: Usando ''' você consegue fazer um grande texto até que feche
#o mesmo.

#Ex.

'''

Eu quero
Café

'''


#Criar variáveis é dar valor para coisas em geral

#Ex. 
nome = 'Jairon'
idade = 18
altura = 1.70
peso = 83

#Podendo fazer cálculos com eles 
#Obs.: Com valores que possui virgula, antes do parênteses é
#necessário colocar um float, para identificar que ele é decimal

print(float((idade + altura) / 2))

#Se pode também usar o sistema do f string para colocar
#variáveis em determinados locais que você deseja, com o valor delas

#Ex.:

print(f'{nome} tem {idade} anos e possui {altura} de altura')

#Uma informação interessante é os tipos de dados que temos no python
#Ao menos só os iniciais 

inteiro = 5 # int
real = 5.5 # float
booleano = True # bool
texto = 'Olá' # str

#O input é o comando para você colocar um dado dentro do programa
#como por exemplo.

#Ex.:

input('Digite algo aceitável')

#Porém, podemos fazer o input colocar informações em uma variável
#como em

#Ex.: 

vida = input('Digite algo que te lembra a vida')

#OBS.: Lembrando que para valores flutuantes ou inteiros, usamos
#respectivamente:

dados = float(input())

dados_inteiros = int(input())

#condições são metodos de checagem que usam index
#Eles são.:

# IF (Se) = 
# 
#Ex.: 

if 2 == 2:
    print('Verdadeiro')

# ELIF (Se não, se) =

if 2 == 2:
    print('Verdadeiro')
elif 2 == 3:
    print('Falso')
elif 2 == 4:
    print('Falso também')
 
# ELSE (Se não) =

if 2 == 2:
    print('Verdadeiro')
else:
    print('Falso')  

#IF é usado para checagem única, quando se vai começar a checagem.
# Se por acaso você precisar fazer várias checagens ao mesmo tempo.
# Pois o ELIF é focado em checagem em cadeia com várias variáveis e 
# Situações. O ELSE é usado na maioria das vezes para situações em 
# Geral e finalizar o código com alguma situação, sempre sendo usado
# Quando nenhumas das outras checagem deram certo, os IF e ELIF
# 
#Operadores Relacionais são feitos para comparação onde mostro alguns deles
#Obs.: É preciso lembrar que eles usam valores booleanos de True e False

# == Esse valor pergunta se um número é igual a outro:

# 2 == 2?

# > Maior que:

# 2 > 2?
 
# >= Maior ou igual:

# 2 >= 2?
 
# < Menor que:
 
# 2 < 2?
 
# <= Menor ou Igual:
 
# 2 <= 2?
 
# != Diferente:
 
# 2 != 2?
 

# Operadores lógicos são usados para fazer várias comparações dentro dos if
# ou analisar se algo está ou não está

# 'and' Faz duas comparações entre valores
 
# a == b and b == c 
#Obs.: Lembrando, que se uma das duas comparações for falsa o valor
# Booleano retornado será de False. Para toda a setença ser con-
# siderada verdadeira é necessário que as duas sejam verdadeiras

# 'or' Faz comparações vendo se ou é um, ou outro das setenças são verdadeiras

# a == b or c == d
#Obs.: Já nesse caso, se sómente uma delas for verdadeira, toda a sentença
# Será considerada verdadeira.
 
# 'not' Retorna falso se o valor for verdadeiro.
 
# 'is' É usado para ver se algo é ou não é, usado em comparação.
 
# 'is not' É usado para o inverso do primeiro
 
# 'in' É para encontrar um valor em algum segmento ou lista 

# 'in not' É o inverso do primeiro já dito
#  
# 
# Para formatar valores usamos algumas linguagens no python:

# :s (Para textos) 

# :d (para inteiros)

# :f (Para floats)

# :.(Número)f (Para contar casas decimais)

# :(Caractere) (< ou > ou ^) (Quantidade) (Tipo - s, d ou f)     
# 
# Ex.:
# 
divid = 3.3333333355

print(f'{divid:.2f}')

