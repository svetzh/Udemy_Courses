class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
        else:
            new_node.next = self.first
            self.first = new_node
        self.length += 1


my_que = Queue(44)
my_que.push(99)
my_que.push(53)
my_que.push(8)

my_que.print_queue()