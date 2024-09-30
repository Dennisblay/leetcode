from unittest import TestCase, main


class TestNode(TestCase):
    def test_node_value(self):
        import exercise
        node = exercise.Node(1)
        self.assertEqual(node.value, 1)

    def test_node_next(self):
        import exercise
        node1 = exercise.Node(1)
        self.assertIsNone(node1.next)
        node2 = exercise.Node(2)
        node1.next = node2
        self.assertEqual(node1.next, node2)


class TestLinkedList(TestCase):
    def test_initialization_of_linked_list(self):
        import exercise
        linked_list = exercise.LinkedList(1)
        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.tail.value, 1)
        self.assertEqual(linked_list.length, 1)

    def test_head(self):
        import exercise
        linked_list = exercise.LinkedList(1)
        self.assertEqual(linked_list.head.value, 1)

    def test_tail(self):
        import exercise
        linked_list = exercise.LinkedList(1)
        self.assertEqual(linked_list.tail.value, 1)

    def test_length(self):
        import exercise
        linked_list = exercise.LinkedList(1)
        self.assertEqual(linked_list.length, 1)

    def test_append_single_node_to_empty_list(self):
        import exercise
        ll = exercise.LinkedList(5)
        ll.make_empty()
        ll.append(3)

        self.assertEqual(ll.head.value, 3)
        self.assertEqual(ll.tail.value, 3)
        self.assertEqual(ll.length, 1)

    def test_append_multiple_nodes_to_empty_list(self):
        import exercise
        ll = exercise.LinkedList(5)
        ll.make_empty()
        values_to_append = [3, 4, 5, 6]
        for value in values_to_append:
            ll.append(value)

        result = []
        current = ll.head
        while current:
            result.append(current.value)
            current = current.next
        self.assertEqual(result, values_to_append)
        self.assertEqual(ll.length, 4)

    def test_append_to_non_empty_list(self):
        import exercise
        ll = exercise.LinkedList(1)
        values_to_append = [2, 3, 4]
        for value in values_to_append:
            ll.append(value)

        result = [1] + values_to_append
        current_values = []
        current = ll.head
        while current:
            current_values.append(current.value)
            current = current.next
        self.assertEqual(current_values, result)
        self.assertEqual(ll.tail.value, values_to_append[-1])
        self.assertEqual(ll.length, 4)

    def test_tail_and_length_updated_appropriately(self):
        import exercise
        ll = exercise.LinkedList(5)
        ll.append(6)

        self.assertEqual(ll.tail.value, 6)
        self.assertEqual(ll.length, 2)

    def test_pop_on_linked_list_with_one_node(self):
        import exercise
        linked_list = exercise.LinkedList(1)
        popped_node = linked_list.pop()
        self.assertEqual(popped_node.value, 1)
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)
        self.assertEqual(linked_list.length, 0)

    def test_pop_on_linked_list_with_multiple_nodes(self):
        import exercise
        linked_list = exercise.LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        popped_node = linked_list.pop()
        self.assertEqual(popped_node.value, 3)
        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.tail.value, 2)
        self.assertEqual(linked_list.length, 2)

    def test_pop_on_empty_linked_list(self):
        import exercise
        linked_list = exercise.LinkedList(1)
        linked_list.head = None
        linked_list.tail = None
        linked_list.length = 0
        popped_node = linked_list.pop()
        self.assertIsNone(popped_node)
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)
        self.assertEqual(linked_list.length, 0)

    def test_pop_all(self):
        import exercise
        linked_list = exercise.LinkedList(1)
        linked_list.append(2)
        popped_node = linked_list.pop()
        self.assertEqual(popped_node.value, 2)
        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.tail.value, 1)
        self.assertEqual(linked_list.length, 1)
        popped_node = linked_list.pop()
        self.assertEqual(popped_node.value, 1)
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)
        self.assertEqual(linked_list.length, 0)
        popped_node = linked_list.pop()
        self.assertIsNone(popped_node)
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)
        self.assertEqual(linked_list.length, 0)

    def test_prepend_single_node_to_empty_list(self):
        import exercise
        ll = exercise.LinkedList(5)
        ll.pop()  # Making the list empty.
        ll.prepend(3)

        self.assertEqual(ll.head.value, 3)
        self.assertEqual(ll.tail.value, 3)
        self.assertEqual(ll.length, 1)

    def test_prepend_multiple_nodes_to_empty_list(self):
        import exercise
        ll = exercise.LinkedList(5)
        ll.pop()  # Making the list empty.
        values_to_prepend = [3, 2, 1]
        for value in values_to_prepend:
            ll.prepend(value)

        # We expect the list values to be reversed because we're prepending.
        result = list(reversed(values_to_prepend))
        current = ll.head
        current_values = []
        while current:
            current_values.append(current.value)
            current = current.next
        self.assertEqual(current_values, result)
        self.assertEqual(ll.length, 3)

    def test_prepend_to_non_empty_list(self):
        import exercise
        ll = exercise.LinkedList(4)
        values_to_prepend = [3, 2, 1]
        for value in values_to_prepend:
            ll.prepend(value)

        # We expect the list values to be reversed because we're prepending.
        result = list(reversed(values_to_prepend)) + [4]
        current_values = []
        current = ll.head
        while current:
            current_values.append(current.value)
            current = current.next
        self.assertEqual(current_values, result)
        self.assertEqual(ll.head.value, values_to_prepend[-1])
        self.assertEqual(ll.length, 4)

    def test_head_and_length_updated_appropriately(self):
        import exercise
        ll = exercise.LinkedList(5)
        ll.prepend(4)

        self.assertEqual(ll.head.value, 4)
        self.assertEqual(ll.length, 2)

    def test_pop_first_from_empty_list(self):
        import exercise
        ll = exercise.LinkedList(5)
        ll.pop()
        result = ll.pop_first()

        self.assertIsNone(result)
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
        self.assertEqual(ll.length, 0)

    def test_pop_first_from_single_node_list(self):
        import exercise
        ll = exercise.LinkedList(5)
        removed_node = ll.pop_first()

        self.assertEqual(removed_node.value, 5)
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
        self.assertEqual(ll.length, 0)

    def test_pop_first_from_multiple_nodes_list(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        removed_node = ll.pop_first()

        self.assertEqual(removed_node.value, 1)
        self.assertEqual(ll.head.value, 2)
        self.assertEqual(ll.tail.value, 3)
        self.assertEqual(ll.length, 2)

    def test_properties_after_pop_first(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.pop_first()
        ll.pop_first()

        self.assertEqual(ll.head.value, 3)
        self.assertEqual(ll.tail.value, 3)
        self.assertEqual(ll.length, 1)

    def test_get_with_negative_index(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        result = ll.get(-1)

        self.assertIsNone(result)

    def test_get_with_out_of_bound_index(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        result = ll.get(5)

        self.assertIsNone(result)

    def test_get_first_node(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        node = ll.get(0)

        self.assertIsNotNone(node)
        self.assertEqual(node.value, 1)

    def test_get_middle_node(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        node = ll.get(1)

        self.assertIsNotNone(node)
        self.assertEqual(node.value, 2)

    def test_get_last_node(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        node = ll.get(2)

        self.assertIsNotNone(node)
        self.assertEqual(node.value, 3)

    def test_get_node_from_empty_list(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.pop()
        result = ll.get(0)

        self.assertIsNone(result)

    def test_set_value_with_negative_index(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        result = ll.set_value(-1, 10)

        self.assertFalse(result)

    def test_set_value_with_out_of_bound_index(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        result = ll.set_value(5, 10)

        self.assertFalse(result)

    def test_set_value_of_first_node(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        result = ll.set_value(0, 10)

        self.assertTrue(result)
        self.assertEqual(ll.get(0).value, 10)

    def test_set_value_of_middle_node(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        result = ll.set_value(1, 20)

        self.assertTrue(result)
        self.assertEqual(ll.get(1).value, 20)

    def test_set_value_of_last_node(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        result = ll.set_value(2, 30)

        self.assertTrue(result)
        self.assertEqual(ll.get(2).value, 30)

    def test_set_value_on_empty_list(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.pop()
        result = ll.set_value(0, 10)

        self.assertFalse(result)

    def test_insert_with_negative_index(self):
        pass
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        result = ll.insert(-1, 10)

        self.assertFalse(result)
        self.assertEqual(ll.length, 3)  # No change in length

    def test_insert_with_out_of_bound_index(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        result = ll.insert(4, 10)  # 4 is out of bounds for a list of length 3

        self.assertFalse(result)
        self.assertEqual(ll.length, 3)  # No change in length

    def test_insert_at_start_of_list(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        result = ll.insert(0, 10)

        self.assertTrue(result)
        self.assertEqual(ll.get(0).value, 10)

    def test_insert_in_middle_of_list(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        result = ll.insert(1, 20)

        self.assertTrue(result)
        self.assertEqual(ll.get(1).value, 20)

    def test_insert_at_end_of_list(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        result = ll.insert(2, 30)  # 3 is at the end of the list with length 3

        self.assertTrue(result)
        self.assertEqual(ll.get(2).value, 30)

    def test_insert_on_empty_list(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.pop_first()
        result = ll.insert(0, 10)

        self.assertFalse(result)
        # self.assertEqual(ll.get(0).value, 10)
        # self.assertEqual(ll.length, 1)  # Length should be 1 now


class TestRemoveMethod(TestCase):

    def test_remove_with_negative_index(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        removed_node = ll.remove(-1)

        self.assertIsNone(removed_node)
        self.assertEqual(ll.length, 3)  # No change in length

    def test_remove_with_out_of_bound_index(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        removed_node = ll.remove(3)  # 3 is out of bounds for a list of length 3

        self.assertIsNone(removed_node)
        self.assertEqual(ll.length, 3)  # No change in length

    def test_remove_at_start_of_list(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        removed_node = ll.remove(0)

        self.assertEqual(removed_node.value, 1)
        self.assertEqual(ll.get(0).value, 2)

    def test_remove_in_middle_of_list(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        removed_node = ll.remove(1)

        self.assertEqual(removed_node.value, 2)
        self.assertNotEqual(ll.get(1).value, 2)
        self.assertEqual(ll.get(1).value, 3)

    def test_remove_at_end_of_list(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        removed_node = ll.remove(2)  # 2 is at the end of the list with length 3

        self.assertEqual(removed_node.value, 3)
        self.assertIsNone(ll.get(2))

    def test_remove_on_empty_list(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.pop_first()
        removed_node = ll.remove(0)

        self.assertIsNone(removed_node)
        self.assertEqual(ll.length, 0)  # Length should remain 0

    def test_reverse_single_element_list(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.reverse()

        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 1)
        self.assertEqual(ll.length, 1)  # Length should remain 1

    def test_reverse_two_element_list(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.reverse()

        self.assertEqual(ll.head.value, 2)
        self.assertEqual(ll.tail.value, 1)
        self.assertEqual(ll.length, 2)  # Length should remain 2

    def test_reverse_multi_element_list(self):
        import exercise
        ll = exercise.LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.reverse()

        self.assertEqual(ll.head.value, 3)
        self.assertEqual(ll.tail.value, 1)
        self.assertEqual(ll.get(1).value, 2)
        self.assertEqual(ll.length, 3)  # Length should remain 3


if __name__ == "__main__":
    main()
