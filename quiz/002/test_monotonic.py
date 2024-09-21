import unittest

from monotonic import is_monotonic


class TestMonotonic(unittest.TestCase):

    def test_monotonic_unique_values(self):
        # Test monotonic increasing values
        array = [1, 2, 3]
        self.assertTrue(is_monotonic(array), f"Passed: {array} is monotonic")

    def test_monotonic_duplicate_values(self):
        # Test elements with duplicate values
        array = [1, 3, 3, 3, 4, 4]
        self.assertTrue(is_monotonic(array), f"Passed: {array} is monotonic")

    def test_monotonic_all_duplicate_values(self):
        # Test elements with all being duplicate values
        array = [3, 3, 3, 3, 3, 3]
        self.assertTrue(is_monotonic(array), f"Passed: {array} is monotonic")

    def test_monotonic_all_but_one_duplicate_values(self):
        # Test elements with all but one value not duplicate
        array = [3, 3, 3, 3, 9, 3]
        self.assertFalse(is_monotonic(array), f"Passed: {array} is not monotonic")

    def test_monotonic_with_negative_at_end(self):
        # Test elements with all but one value not duplicate
        array = [3, 3, 3, 3, 2, -3]
        self.assertTrue(is_monotonic(array), f"Passed: {array} is not monotonic")

    def test_non_monotonic(self):
        # Test for non-monotonic array
        array = [1, 2, 3, 3, 2, 1, 3]
        self.assertFalse(is_monotonic(array), f"Passed {array} is  not monotonic")

    def test_monotonic_single_value(self):
        # Test for array with a single value
        array = [0]
        self.assertTrue(is_monotonic(array), f"Passed {array} is  monotonic")

    def test_monotonic_empty_value(self):
        # Test for empty array
        array = []
        self.assertTrue(is_monotonic(array), f"Passed {array} is  monotonic")


if __name__ == '__main__':
    unittest.main()
