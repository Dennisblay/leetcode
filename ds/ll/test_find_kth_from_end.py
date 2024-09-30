from unittest import TestCase, main


class TestFindKthFromEnd(TestCase):

    def test_k_less_than_length(self):
        import exercise
        ll = exercise.LinkedList(1)
        for i in range(2, 6):  # Create a linked list: 1->2->3->4->5
            ll.append(i)
        kth_node = exercise.find_kth_from_end(ll, 2)
        self.assertEqual(kth_node.value, 4)  # 4 is the 2nd node from the end

    def test_k_equal_to_length(self):
        import exercise
        ll = exercise.LinkedList(1)
        for i in range(2, 6):  # Create a linked list: 1->2->3->4->5
            ll.append(i)
        kth_node = exercise.find_kth_from_end(ll, 5)
        self.assertEqual(kth_node.value, 1)  # 1 is the 5th node from the end

    def test_k_more_than_length(self):
        import exercise
        ll = exercise.LinkedList(1)
        for i in range(2, 6):  # Create a linked list: 1->2->3->4->5
            ll.append(i)
        kth_node = exercise.find_kth_from_end(ll, 10)
        self.assertIsNone(kth_node)  # There is no 10th node from the end

    def test_empty_list(self):
        import exercise
        ll = exercise.LinkedList(1)
        kth_node = exercise.find_kth_from_end(ll, 1)
        self.assertEqual(kth_node.value, 1)  # 1 is the only node in the list


if __name__ == "__main__":
    main()
