from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int):
    """
    Merges nums2 into nums1 in-place, assuming nums1 has enough space (size of m+n).
    """
    combined = m + n - 1  # The last index in the combined array
    i = m - 1  # Last index of the valid elements in nums1
    j = n - 1  # Last index of nums2

    while j >= 0:  # Only need to worry about nums2 because nums1 is already in place
        if nums1[i] > nums2[j]:
            nums1[combined] = nums1[i]  # Move larger element from nums1
            i -= 1
        else:
            nums1[combined] = nums2[j]  # Move element from nums2
            j -= 1
        combined -= 1


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        combined: int = (m + n) - 1  # zero-indexed
        i = m - 1
        j = n - 1
        while i >= 0 or j >= 0:
            if j >= 0 and nums2[j] > nums1[i]:
                nums1[combined] = nums2[j]
                j -= 1
            else:
                nums1[combined] = nums1[i]
                i -= 1

            combined -= 1


# class Solution(object):
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         combined: int = (m + n) - 1  # zero-indexed
#         i = m - 1
#         j = n - 1
#         while i >= 0 or j >= 0:
#             if j >= 0 and nums2[j] > nums1[i]:
#                 nums1[combined] = nums2[j]
#                 j -= 1
#             else:
#                 nums1[combined] = nums1[i]
#                 i -= 1
#
#             combined -= 1


if __name__ == "__main__":
    arr1 = [1, 2, 3, 0, 0, 0]
    arr2 = [2, 5, 6]
    merge(arr1, 3, arr2, 3)
    print(arr1)
    # soln = Solution()
    # soln.merge(arr1, 3, arr2, 3)
    # print(arr1)
