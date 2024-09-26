import unittest

from permute import permute_unique


class TestPermuteFunction(unittest.TestCase):

    def test_single_element_array(self):
        self.assertEqual(permute_unique([1]), [[1]], "Failed with single element array")

    def test_multiple_elements_array(self):
        result = permute_unique([1, 2, 3])
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertTrue(all(item in result for item in expected), "Failed with multiple elements array")

    def test_unique_permutations(self):
        nums = [1, 2, 3]
        result = permute_unique(nums)
        unique_results = [list(x) for x in set(tuple(x) for x in result)]
        self.assertEqual(len(result), len(unique_results), "Permutations are not unique")

    def test_permutations_count(self):
        nums = [1, 2, 3]
        result = permute_unique(nums)
        expected_count = 6  # 3! = 6
        self.assertEqual(len(result), expected_count, "Incorrect number of permutations")


if __name__ == "__main__":
    unittest.main()
