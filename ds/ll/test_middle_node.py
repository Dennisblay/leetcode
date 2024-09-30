from unittest import TestCase, main


def get_list_values(ll):
    values = []
    temp = ll.head
    while temp:
        values.append(temp.value)
        temp = temp.next
    return values


class TestFindMiddleNode(TestCase):

    def test_single_node(self):
        import middle_node
        ll = middle_node.LinkedList(1)
        middle_node = ll.find_middle_node()
        self.assertEqual(middle_node.value, 1)

    def test_even_number_of_nodes(self):
        import middle_node
        ll = middle_node.LinkedList(1)
        for val in [2, 3, 4]:
            ll.append(val)
        middle_node = ll.find_middle_node()
        # In the case of even nodes, the second middle value will be returned.
        # Here, for [1, 2, 3, 4], 3 will be returned.
        self.assertEqual(middle_node.value, 3)

    def test_odd_number_of_nodes(self):
        import middle_node
        ll = middle_node.LinkedList(1)
        for val in [2, 3, 4, 5]:
            ll.append(val)
        middle_node = ll.find_middle_node()
        # In the case of odd nodes, the exact middle value will be returned.
        # Here, for [1, 2, 3, 4, 5], 3 will be returned.
        self.assertEqual(middle_node.value, 3)


if __name__ == '__main__':
    main()
