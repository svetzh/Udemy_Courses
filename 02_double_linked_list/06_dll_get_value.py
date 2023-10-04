class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def get_value(self, idx):
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


my_dll = DoublyLinkedList(10)
my_dll.append(41)
my_dll.append(65)
my_dll.append(87)


print(my_dll.get_value(1))
print(my_dll.get_value(2))


