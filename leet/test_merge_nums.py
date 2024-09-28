import unittest

from merge_nums import merge


class TestMergeNums(unittest.TestCase):
    def test_example_1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        merge(nums1, 3, nums2, 3)
        # After merging, nums1 should be [1, 2, 2, 3, 5, 6]
        expected = [1, 2, 2, 3, 5, 6]
        self.assertEqual(nums1, expected)

    def test_example_2(self):
        nums1 = [1]
        nums2 = []
        merge(nums1, 1, nums2, 0)
        # After merging, nums1 should be [1, 2, 2, 3, 5, 6]
        expected = [1]
        self.assertEqual(nums1, expected)

    def test_example_3(self):
        nums1 = [0]
        nums2 = [1]
        merge(nums1, 0, nums2, 1)
        # After merging, nums1 should be [1, 2, 2, 3, 5, 6]
        expected = [1]
        self.assertEqual(nums1, expected)


if __name__ == "__main__":
    unittest.main()
