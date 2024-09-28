import unittest
from combination_sum_unique import combination_sum_unique

class TestCombinationSum2(unittest.TestCase):
    def test_example_1(self):
        candidates = [10,1,2,7,6,1,5]
        target = 8
        expected = [[1,1,6],[1,2,5],[1,7],[2,6]]
        result = combination_sum_unique(candidates, target)
        self.assertEqual(sorted(result), sorted(expected), f"Failed for candidates {candidates} with target {target}")

    def test_example_2(self):
        candidates = [2,5,2,1,2]
        target = 5
        expected = [[1,2,2],[5]]
        result = combination_sum_unique(candidates, target)
        self.assertEqual(sorted(result), sorted(expected), f"Failed for candidates {candidates} with target {target}")

    def test_no_combinations(self):
        candidates = [2,4,6]
        target = 5
        expected = []
        result = combination_sum_unique(candidates, target)
        self.assertEqual(sorted(result), sorted(expected), f"Failed for candidates {candidates} with target {target}, expected no combinations")

    def test_single_candidate_equals_target(self):
        candidates = [5]
        target = 5
        expected = [[5]]
        result = combination_sum_unique(candidates, target)
        self.assertEqual(sorted(result), sorted(expected), f"Failed when single candidate equals target")

    def test_all_candidates_equals_target(self):
        candidates = [1,1,1,1,1]
        target = 5
        expected = [[1,1,1,1,1]]
        result = combination_sum_unique(candidates, target)
        self.assertEqual(sorted(result), sorted(expected), f"Failed when all candidates sum to target")

    def test_duplicates_in_candidates(self):
        candidates = [1,2,2,2,5]
        target = 5
        expected = [[1,2,2],[5]]
        result = combination_sum_unique(candidates, target)
        self.assertEqual(sorted(result), sorted(expected), f"Failed to handle duplicates correctly")

if __name__ == '__main__':
    unittest.main()