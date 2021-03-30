def search(list, element):
    """
        Retorna o índice do elemento que estiver na lista ou None, caco contrário
    """
    for i in range(len(list)):
        if list[i] == element:
            return i
    return None

list_test = [8, "5", 32, 0, "python", 11]
element = 11

index = search(list_test, element)

if index is not None:
    print("O índice do elemento {} é {}".format(element, index))
else:
    print("O elemento {} não se encontra na lista".format(element))