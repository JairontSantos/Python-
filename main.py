
class Node:
    def __init__(self, numero, proximo=None):
        self.numero = numero
        self.proximo = proximo

class ListaEncadeada:

    tamanho = 0

    def __init__(self, head=None):
        self.head = head
        if head is not None:
            self.tamanho += 1
    
    def print(self):
        """ Printa todos os elementos da lista """

        # Se a lista está vazia, não fazer nada
        if self.head is None:
            return
        
        """ 
        O nome tmp vem de "temporária". Vamos usar essa variável para iterar
        por cada elemento presente na lista. Chegamos ao fim quando o elemento
        presente em tmp ser None (pois o último node aponta para 'None' como
        próximo elemento).
        """
        
        # Iniciando tmp para o primeiro elemento
        tmp = self.head
        # Printando o número contido no elemento e trocando o valor de tmp
        # para o próximo elemento até que cheguemos ao fim da lista
        while tmp is not None:
            print(tmp.numero)
            tmp = tmp.proximo
    
    def append(self, numero):
        """ Adiciona numero ao fim da lista """
        
        node = Node(numero)
        
        """ Se a lista está vazia, o node será a cabeça. Se não, usaremos
        o mesmo raciocínio usado no método 'print' para percorrer toda a 
        lista. A única mudança é que chegaremos se o PRÓXIMO elemento é
        None, já que iremos o substituir. """
        if self.head is None:
            self.head = node
        else:
            tmp = self.head
            while tmp.proximo is not None:
                tmp = tmp.proximo
            
            tmp.proximo = node
            self.tamanho += 1

    def insert(self, numero):
        """ Adiciona número ao início da lista """

        node = Node(numero)
        
        # Se a lista está vazia, o node será a cabeça
        if self.head is None:
            self.head = node
        else:
            node.proximo = self.head
            self.head = node
            self.tamanho += 1
        
    def delete(self, index):
        """ Deleta o elemento de número 'index' da lista """
        
        # Se a lista está vazia ou é menor do que o index passado,
        # não fazer nada
        if self.head is None or index > self.tamanho:
            return
        
        """ Mesmo raciocínio usado nas funções anteriores, mas agora
        podemos usar um for loop. Removemos 1 do index pois queremos
        iterar até o elemento anterior, e fazê-lo apontar para o
        elemento após o próximo """
        index -= 1
        if index == -1:
            self.head = self.head.proximo
        else:
            tmp = self.head
            for i in range(index):
                tmp = tmp.proximo
            
            tmp.proximo = tmp.proximo.proximo
        self.tamanho -= 1


lista = ListaEncadeada(Node(1))

lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)
lista.append(6)
lista.insert(10)

lista.delete(1)

lista.print()
print(f'Tamanho: {lista.tamanho}')
