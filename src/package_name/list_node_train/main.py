if __name__ == '__main__':
    from linked_list import LinkedList

    my_list = LinkedList()

    my_list.append(-2)
    my_list.append(0)
    my_list.append(4)
    my_list.append(8)
    my_list.append(16)

    my_list.show()
    print(my_list.value_at(1))
    my_list.show()
    my_list.lenghth()

