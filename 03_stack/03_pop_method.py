class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def popp(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp


my_stck = Stack(5)
my_stck.push(15)
my_stck.push(25)
my_stck.push(35)

my_stck.popp()
my_stck.print_stack()

