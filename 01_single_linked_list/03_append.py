class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)  # created a node
        if self.head is None:  # check if the key is empty
            self.head = new_node
            self.tail = new_node
        else:  #
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True  # for future methods that will require true or false statements to be returned


my_ll = LinkedList(11)
my_ll.append(2)
my_ll.print_list()
