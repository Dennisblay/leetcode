import unittest
from permute import permute_duplicates


class TestPermuteUniqueFunction(unittest.TestCase):

    def test_single_element_array(self):
        self.assertEqual(permute_duplicates([1]), [[1]], "Failed with single element array")

    def test_multiple_elements_no_duplicates(self):
        result = permute_duplicates([1, 2, 3])
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertTrue(all(item in result for item in expected), "Failed with multiple elements without duplicates")

    def test_multiple_elements_with_duplicates(self):
        result = permute_duplicates([1, 1, 2])
        expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        self.assertTrue(all(item in result for item in expected), "Failed with multiple elements with duplicates")

    def test_unique_permutations(self):
        nums = [1, 1, 2]
        result = permute_duplicates(nums)
        unique_results = [list(x) for x in set(tuple(x) for x in result)]
        self.assertEqual(len(result), len(unique_results), "Permutations are not unique")

    def test_permutations_count_with_duplicates(self):
        nums = [1, 1, 2]
        result = permute_duplicates(nums)
        expected_count = 3  # There are 3 unique permutations for [1, 1, 2]
        self.assertEqual(len(result), expected_count, "Incorrect number of unique permutations for array with duplicates")

if __name__ == '__main__':
    unittest.main()