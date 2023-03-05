#No começo de tudo sempre terá um Head, que seria o primeiro nó, e somente com ele se inicia a lista

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None #Representa um node 
# Aqui criei uma classe que define o Node 

class LinkedList:
    def __init__(self):
        self.head = None #Aqui começa vazio pois a lista começa sem nada, até que o primeiro Node que é o Head seja implementado, para começar o processo
        self.size = 0
# Aqui cria uma lista encadeada, onde podemos iremos linkar um Node ao outro

    def push(self, node: Node):
        # No segundo valor colocamos os : para associar o node á classe Node
        if (self.head == None):
            self.head = node 
            # Aqui se liga o primeiro node como head
            return

        node.next = self.head
        #Aqui estamos colocando o novo node para ser o novo Head, absorvendo as informações dele 
        self.head = node
        #Aqui é o head apontando para o node que vai ser incluido na lista

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

mylist = LinkedList()

#teste
if mylist.size == 0:
    mylist.push(node1)
    mylist.push(node2)

print(node1.value)