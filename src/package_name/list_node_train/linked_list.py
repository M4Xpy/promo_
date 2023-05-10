from class_node import Node


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        curr_node = self.head
        if not curr_node:
            self.head = new_node
            return
        while curr_node.get_next():
            curr_node = curr_node.get_next()
        curr_node.set_next(new_node)

    def show(self):
        curr_node = self.head
        output = ''
        while curr_node:
            output += f'{curr_node.get_data()} -> '
            curr_node = curr_node.get_next()
        print(output)

    def lenghth(self):
        curr_node = self.head
        count = 0
        while curr_node:
            count += 1
            curr_node = curr_node.get_next()
        print(count)

    def push_front(self, data):
        new_node = Node(data)
        curr_node = self.head
        new_node.set_next(curr_node)
        self.head = new_node

    def remove_back(self):
        curr_node = self.head
        while curr_node.get_next().get_next():
            curr_node = curr_node.get_next()
        curr_node.set_next(None)

    def remove_front(self):
        # self.head = self.head.get_next()
        curr_node = self.head
        self.head = curr_node.get_next()

    def value_at(self, index):
        curr_node = self.head
        count = 0
        while curr_node :
            if count == index:
                return curr_node.get_data()
            count += 1
            curr_node = curr_node.get_next()
        print('index is out of range')

    def value__index(self, index):
        curr_node = self.head

        for _ in range(index):
            if curr_node != None:
                curr_node = curr_node.get_next()
            else:
                print('index is out of range')
                return None
        return curr_node.get_data()

    def insert(self, index, data):
        new_node = Node(data)
        curr_node = self.head
        count = 0
        while curr_node.get_next():
            if not index:
                self.push_front(data)
                return
            elif -~count == index:
                node_after_curr = curr_node.get_next()
                curr_node.set_next(new_node)
                new_node.set_next(node_after_curr)
                return
            count += 1
            curr_node = curr_node.get_next()
        print('index out of range')

    def remove(self, index):
        curr_node = self.head
        count = 0
        while curr_node.get_next():
            if not index:
                self.remove_front()
                return
            elif -~count == index:
                node_to_remove = curr_node.get_next()
                node_after_removed = node_to_remove.get_next()
                curr_node.set_next(node_after_removed)
                return
            count += 1
            curr_node = curr_node.get_next()
        print('index out of range')

    def reverse(self):
        prev = None
        curr_node = self.head
        next = Node
        while curr_node:
            next = curr_node.get_next()
            curr_node.set_next(prev)
            prev = curr_node
            curr_node = next
        self.head = prev



