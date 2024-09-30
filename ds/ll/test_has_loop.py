from unittest import TestCase, main


class TestHasLoop(TestCase):

    def test_no_nodes(self):
        import exercise
        ll = exercise.LinkedList(1)
        for i in range(1):
            ll.append(i)
        self.assertFalse(ll.has_loop())

    def test_no_loop(self):
        import exercise
        ll = exercise.LinkedList(1)
        for i in range(1, 5):
            ll.append(i)
        self.assertFalse(ll.has_loop())

    # def test_has_loop(self):
    #     import exercise
    #     ll = exercise.LinkedList(1)
    #     for i in range(1, 5):
    #         ll.append(i)
    #     # Manually create a loop for testing
    #     ll.tail.next = ll.head.next.next
    #     self.assertTrue(ll.has_loop())

    # Helper function to create a partial loop
    @staticmethod
    def create_partial_loop(linked_list):
        linked_list.head.next.next.next.next = linked_list.head.next

    # Test case for has_loop method
    def test_has_loop(self):
        import exercise
        # Create linked list with 8 elements
        long_list = exercise.LinkedList(1)
        for i in range(2, 9):  # Loop from 2 to 8
            long_list.append(i)

        # Create a loop in the first half
        self.create_partial_loop(long_list)

        # Create second half list with no loop
        second_half = exercise.LinkedList(5)
        for i in range(6, 9):  # Loop from 6 to 8
            second_half.append(i)

        # Check if has_loop returns True for list with a loop
        self.assertTrue(long_list.has_loop())

        # Check if has_loop returns False for list without a loop
        self.assertFalse(second_half.has_loop())

if __name__ == "__main__":
    main()
