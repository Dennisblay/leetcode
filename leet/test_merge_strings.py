import unittest

from merge_strings import merge_strings_recur


class TestMergeStrings(unittest.TestCase):

    def test_equal_length(self):
        self.assertEqual(merge_strings_recur("abc", "pqr"), "apbqcr")

    def test_word2_greater_in_length(self):
        self.assertEqual(merge_strings_recur("ab", "pqrs"), "apbqrs")

    def test_word1_greater_in_length(self):
        self.assertEqual(merge_strings_recur("abcd", "pq"), "apbqcd")


if __name__ == "__main__":
    unittest.main()
