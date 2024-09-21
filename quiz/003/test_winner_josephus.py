import unittest
from unittest import TestCase

from winner_josephus import winner_iterative  # Import findTheWinner function


class Evaluate(TestCase):

    def test_basic_case(self):
        self.assertEqual(winner_iterative(4, 2), 1, "findTheWinner(4, 2) should return 1")

    def test_single_friend(self):
        self.assertEqual(winner_iterative(1, 5), 1, "findTheWinner(1, 5) should return 1")

    def test_k_greater_than_n(self):
        self.assertEqual(winner_iterative(5, 10), 4, "findTheWinner(5, 10) should return 4")

    def test_k_is_one(self):
        self.assertEqual(winner_iterative(6, 1), 6, "findTheWinner(6, 1) should return 6")

    def test_large_values(self):
        self.assertEqual(winner_iterative(100, 15), 42, "findTheWinner(100, 15) should return 37")

    def test_n_and_k_equal(self):
        self.assertEqual(winner_iterative(3, 3), 2, "findTheWinner(3, 3) should return 2")

    def test_n_two_k_one(self):
        self.assertEqual(winner_iterative(2, 1), 2, "findTheWinner(2, 1) should return 2")

    def test_n_two_k_two(self):
        self.assertEqual(winner_iterative(2, 2), 1, "findTheWinner(2, 2) should return 1")


if __name__ == "__main__":
    unittest.main()
