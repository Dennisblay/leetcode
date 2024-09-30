from unittest import TestCase

class TestPartitionList(TestCase):

    def setUp(self):
        import exercise
        self.ll = exercise.LinkedList(5)
        for i in [8, 3, 10, 2, 4]:
            self.ll.append(i)
        # LinkedList is 5 -> 8 -> 3 -> 10 -> 2 -> 4

    def test_partition_in_middle(self):
        import exercise
        self.ll.partition_list(5)
        current = self.ll.head
        less_than_5 = True
        while current:
            if current.value >= 5:
                less_than_5 = False
            if less_than_5:
                self.assertLess(current.value, 5)
            else:
                self.assertGreaterEqual(current.value, 5)
            current = current.next

    def test_partition_at_start(self):
        import exercise
        self.ll.partition_list(3)
        current = self.ll.head
        less_than_3 = True
        while current:
            if current.value >= 3:
                less_than_3 = False
            if less_than_3:
                self.assertLess(current.value, 3)
            else:
                self.assertGreaterEqual(current.value, 3)
            current = current.next

    def test_partition_at_end(self):
        import exercise
        self.ll.partition_list(11)
        current = self.ll.head
        while current:
            self.assertLess(current.value, 11)
            current = current.next

    def test_empty_list(self):
        import exercise
        self.ll.make_empty()
        self.ll.partition_list(5)
        self.assertIsNone(self.ll.head)