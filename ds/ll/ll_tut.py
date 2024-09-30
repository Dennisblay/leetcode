from typing import Optional


class Node:
    def __init__(self, value: int, next: Optional['Node'] = None):
        self.value = value
        self.next: Optional['Node'] = next

    def __str__(self):
        return f"Node(value: {self.value}, next: {self.next})"


class LinkedList:

    def __init__(self, value: Optional[int] = None):
        new_node = Node(value=value)
        self.head = new_node
        self.tail = new_node
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

        if self.length == 0:  # if it gets to this point then it means only one item in element even after decrementing
            self.head = None
            self.tail = None

        return temp

    def prepend(self, value):
        new_node = Node(value=value)
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

    def get(self, index: int) -> Optional['Node']:
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index: int, value: int):
        temp = self.get(index=index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index: int, value: int):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length - 1:
            return self.append(value)
        prev = self.get(index - 1)
        curr = prev.next
        prev.next = Node(value=value, next=curr)
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
        return temp

    def reverse(self):
        current = self.head
        self.head = self.tail
        self.tail = current
        after = current.next
        before = None
        for _ in range(self.length):
            after = current.next
            current.next = before
            before = current
            current = after


if __name__ == "__main__":
    ll = LinkedList(0)
    for i in range(1, 10):
        ll.append(i)

    # print(ll.remove(3))

    ll.print()
    ll.reverse()
    ll.print()
