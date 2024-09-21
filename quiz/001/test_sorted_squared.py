import unittest

from sorted_squared import sorted_squared_optimized


class TestSquareAndSort(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(sorted_squared_optimized([]), [])

    def test_single_element_array(self):
        self.assertEqual(sorted_squared_optimized([2]), [4])

    def test_multiple_element_array(self):
        self.assertEqual(sorted_squared_optimized([1, 2, 3, 4]), [1, 4, 9, 16])
        self.assertEqual(sorted_squared_optimized([0, 1, 2, 3]), [0, 1, 4, 9])
        self.assertEqual(sorted_squared_optimized([5, 6, 7, 8]), [25, 36, 49, 64])

    def test_negative_numbers(self):
        self.assertEqual(sorted_squared_optimized([-3, -2, -1, 0]), [0, 1, 4, 9])
        self.assertEqual(sorted_squared_optimized([-5, -4, -3]), [9, 16, 25])

    def test_mixed_numbers(self):
        self.assertEqual(sorted_squared_optimized([-2, 0, 3, 5]), [0, 4, 9, 25])


if __name__ == '__main__':
    unittest.main()
