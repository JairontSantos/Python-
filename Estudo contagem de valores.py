# como encontrar o número/letra com a maior quantidade de aparições 

# Aqui vai criando as váriaveis iniciais da string 
minha_string = 'Eu quero um pouco de whey'
tamanho_string = len(minha_string)

# C vai ser usado no looping, enquanto o resto são variáveis para a encontrar o valor 

c = 0
contagem = 0
letra = ''

# aqui se cria o looping para começar a contagem

while c < tamanho_string:
    conta = minha_string.count(minha_string[c])

    if contagem < conta and minha_string[c].strip():
        letra = minha_string[c]
        contagem = conta


print()