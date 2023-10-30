class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, val):
        new_node = Node(val)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_lst(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.nxt

    def apend(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.nxt = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def get_val(self, idx):
        if idx < 0 or idx >= self.length:
            return None
        temp = self.head
        if idx < self.length / 2:
            for _ in range(idx):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, idx, -1):
                temp = temp.prev
        return temp

    def set_val(self, idx, val):
        temp = self.get_val(idx)
        if temp:
            temp.val = val
            return True
        return False


my_dll = DoublyLinkedList(11)

my_dll.apend(3)
my_dll.apend(22)
my_dll.apend(16)

my_dll.set_val(2, 99)

my_dll.print_lst()