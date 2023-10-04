class Node:
    def __init__(self, value):
        self.value = value
        self.nxt = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.value = value
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.nxt



my_ll = LinkedList.print_list
print(my_ll)
