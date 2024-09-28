import unittest

from combination import combination

class TestCombinationFunction(unittest.TestCase):

    def test_valid_n_k(self):
        self.assertCountEqual(combination(4, 2), [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],
                              "Failed to generate correct combinations for valid n and k.")

    def test_k_equals_zero(self):
        self.assertEqual(combination(4, 0), [[]], "Failed with k equals 0. Should return a list with an empty list.")

    def test_k_equals_n(self):
        self.assertEqual(combination(3, 3), [[1, 2, 3]], "Failed with k equals n. Should return all elements.")

    def test_k_greater_than_n(self):
        self.assertEqual(combination(3, 4), [], "Failed with k greater than n. Should return an empty list.")

    def test_n_equals_zero(self):
        self.assertEqual(combination(0, 0), [[]], "Failed with n equals 0. Should return a list with an empty list.")

    def test_combination_uniqueness_and_completeness(self):
        combinations = combination(4, 3)
        expected_combinations = [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
        for combo in expected_combinations:
            self.assertIn(combo, combinations, f"combination {combo} is missing.")
        self.assertEqual(len(combinations), len(expected_combinations),
                         "Number of combinations is incorrect. Possible duplicates or missing combinations.")

if __name__ == '__main__':
    unittest.main()