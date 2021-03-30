from node import Node
from linked_list import LinkedList

if __name__ == "__main__":
    no1 = Node(5)
    no2 = Node(9)

    print("#" * 10)
    print(no1.data)
    print(no2.data)

    print(no1.next)
    print(no2.next)

    no1.next = no2
    print(no1.next)

    print("#" * 10)
    print("LINKED LIST")

    lista = LinkedList()
    lista.append(1)
    lista.append(2)

    print(lista._size)
    print(lista.head.data)


    print(len(lista))
    lista.append("Nova")
    print(len(lista))

    print(lista[2])
    print(lista.index("Nova"))

    lista.insert(1, "Teste")
    print(lista[1])
    print(lista)

    lista.remove("Teste")
    print(lista[1])

    print(lista)