import unittest
from combination_sum import combination_sum

class TestCombinationSum(unittest.TestCase):
    def test_example_1(self):
        candidates = [2,3,6,7]
        target = 7
        expected = [[2,2,3],[7]]
        result = combination_sum(candidates, target)
        self.assertEqual(sorted(result), sorted(expected), f"Failed for candidates {candidates} with target {target}")

    def test_example_2(self):
        candidates = [2,3,5]
        target = 8
        expected = [[2,2,2,2],[2,3,3],[3,5]]
        result = combination_sum(candidates, target)
        self.assertEqual(sorted(result), sorted(expected), f"Failed for candidates {candidates} with target {target}")

    def test_example_3(self):
        candidates = [2]
        target = 1
        expected = []
        result = combination_sum(candidates, target)
        self.assertEqual(sorted(result), sorted(expected), f"Failed for candidates {candidates} with target {target}")

    def test_empty_candidates(self):
        candidates = []
        target = 7
        expected = []
        result = combination_sum(candidates, target)
        self.assertEqual(sorted(result), sorted(expected), "Failed when candidates are empty")

    def test_target_zero(self):
        candidates = [2,3,5]
        target = 0
        expected = [[]]  # One valid combination: choosing none
        result = combination_sum(candidates, target)
        self.assertEqual(sorted(result), sorted(expected), "Failed when target is zero, expected [[]] indicating no selection")

if __name__ == '__main__':
    unittest.main()