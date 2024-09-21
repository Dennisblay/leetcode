import unittest

from power_sum import power_sum


class TestPowerSum(unittest.TestCase):
    def test_power_sum_single_element_array(self):
        arr = [5]
        result = power_sum(arr)
        self.assertEqual(result, 5, "Expected the sum of a single-element array to be the element itself")

    def test_power_sum_simple_array(self):
        arr = [1, 2, 3]
        result = power_sum(arr)
        self.assertEqual(result, 1 + 2 + 3, "Expected the sum of a simple array to be the sum of its elements")

    def test_power_sum_nested_array(self):
        arr = [2, 3, [4, 1, 2]]
        result = power_sum(arr)
        self.assertEqual(result, 2 + 3 + (4 + 1 + 2) ** 2,
                         "Expected the sum of a nested array to be calculated correctly")

    def test_power_sum_deeply_nested_array(self):
        arr = [1, 2, [7, [3, 4], 2]]
        result = power_sum(arr)
        self.assertEqual(result, 1 + 2 + (7 + (3 + 4) ** 3 + 2) ** 2,
                         "Expected the sum of a deeply nested array to be calculated correctly")


if __name__ == '__main__':
    unittest.main()
