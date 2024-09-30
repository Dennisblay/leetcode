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
        return True

    def make_empty(self):
        self.head = None
        self.tail = None

    def find_middle_node(self) -> Optional['Node']:
        if self.head is None:
            return None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow


if __name__ == "__main__":
    ll = LinkedList(1)
    for i in range(2, 6):
        ll.append(i)

    print(ll.find_middle_node().value)
    ll.print()
