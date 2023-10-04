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
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # def push(self, value):
    #     new_node = Node(value)
    #     if self.length == 0:
    #         self.first = new_node
    #     else:
    #         new_node.next = self.first
    #         self.first = new_node
    #     self.length += 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1


my_q = Queue(42)
my_q.enqueue(6)

my_q.print_queue()
