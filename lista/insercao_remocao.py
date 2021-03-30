#Existe um método chamado insert - my_list.insert(pos, element)
def insert(my_list, element, pos):
    my_list.append(element)

    for i in range(pos, len(my_list) - 1):
        temp = my_list[i]
        my_list[i] = my_list[len(my_list) - 1] 
        my_list[len(my_list) - 1] = temp

    print(my_list)

def remove(my_list, element):
    for i in range(len(my_list) - 1):
        if element == my_list[i]:
            my_list.pop(i)

    print(my_list)

my_list = [1, 2, 3, 4, 5, 6]
print(my_list)
insert(my_list, 7, 3)
remove(my_list, 3)