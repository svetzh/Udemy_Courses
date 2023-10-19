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

    def append_val(self, value):
        new_node = Node(value)  # created a node
        if self.head is None:  # check if the key is empty
            self.head = new_node
            self.tail = new_node
        else:  #
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop_last(self):
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    # this is important

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get_value(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head

        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get_value(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert_value(self, index, value):
        if index < 0 or index > self.length:
            return False  # -> if we're successful in the insert_value method we have to return TRUE otherwise FALSE

        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append_val(value)

        new_node = Node(value)
        temp = self.get_value(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove_item(self, index):
        if index < 0 or index > self.length:
            return None  # -> here we have to return a Node however if we aren't successful we will return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop_last()

        prev = self.get_value(index - 1)
        # temp = self.get_value(index)  # this is O(n)
        temp = prev.next  # O(1)
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse_method(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


my_ll = LinkedList(1)
my_ll.append_val(2)
my_ll.append_val(3)
my_ll.append_val(4)

my_ll.reverse_method()

my_ll.print_list()

