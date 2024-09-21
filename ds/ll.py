from typing import Union, Optional

Ordered = Union[float, str, int]


class Node:
    def __init__(self, value: Ordered, next: Optional['Node'] = None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self):
        self.head: Optional['Node'] = None
        self.size: int = 0

    def push(self, value: Ordered):
        node_to_push = Node(value=value, next=None)
        if self.head is None:
            self.head = node_to_push
            self.size += 1
            return
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = node_to_push
        self.size += 1
        return

    def insert_at_start(self, value: Ordered):
        new_node = Node(value=value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return

    def remove(self, value: Ordered):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return

        current = self.head
        while current is not None:
            if current.next and current.next.value == value:
                prev = current
                prev.next = current.next.next
                self.size -= 1
                return
            current = current.next

    def insert(self, value: Ordered, index: int):
        node_to_insert = Node(value=value, next=None)
        if self.head is None:
            self.head = node_to_insert
            self.size += 1
            return
        current = self.head
        prev: Optional['Node'] = None
        count = 0
        while count <= index and current is not None:
            current = current.next
            count += 1
            if count == index:
                prev = current
                prev.next = node_to_insert
                node_to_insert.next = current.next
                return

    def display(self):
        current = self.head
        while current is not None:
            print(current.value, end=' -> ')
            current = current.next
        print("/")

    @property
    def get_size(self):
        return self.size


if __name__ == "__main__":
    ll = LinkedList()
    for i in range(10):
        ll.push(i)
    ll.display()
    ll.remove(22)
    ll.insert(200, 2)
    # ll.insert_at_start(10)
    ll.display()
