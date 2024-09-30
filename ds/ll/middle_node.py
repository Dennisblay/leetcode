from typing import Optional


class Node:

    def __init__(self, value, next: Optional['Node'] = None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self, value):
        new_node = Node(value=value)
        self.head: Optional['Node'] = new_node
        self.tail: Optional['Node'] = new_node
        self.length = 1

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next

        print("/")

    def append(self, value):
        new_node = Node(value=value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def pop(self):
        if self.head is None:
            return None
        temp = self.head
        prev = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def prepend(self, value):
        new_node = Node(value=value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index: int):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index: int, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index: int, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = Node(value=value, next=temp)
        self.length += 1
        return True

    def remove(self, index: int):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        prev = self.get(index - 1)
        temp = prev.next
        prev.next = prev.next.next
        temp.next = None
        self.length -= 1

    def find_middle_node(self):
        pass


if __name__ == "__main__":
    ll = LinkedList(0)
    for i in range(1, 4):
        ll.append(i)
    ll.remove(2)

    ll.print()
