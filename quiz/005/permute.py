from typing import List

"""
Complexity analysis 
How many steps does it take to generate all permutations (possible arrangements)? 
Given [1, 2, 3]
- For the first element, there'll be 3 choices to pick from. 
- And when we do, there'll be only two choices left to pick from for the second element.
- Only one choice left for the last element.
: 3 x 2 x 1 = 6
So the number of operations to generate all permutations is given as O(!n)
And for each element at position (i), there will be O(n) number of recursive calls until the base condition is met.
T = O(!n x n)
S = O(n)
"""


def permute_unique(arr: List[int]) -> List[List[int]]:
    n = len(arr)
    if n == 1:
        return [[arr[0]]]

    res = []

    def backtrack(i: int):
        if i == n - 1:
            res.append(arr[:])
            return
        for j in range(i, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            backtrack(i + 1)
            arr[i], arr[j] = arr[j], arr[i]

    backtrack(0)
    return res


def permute_duplicates(arr: List[int]) -> List[List[int]]:
    res = []
    n = len(arr)

    def backtrack(i: int):
        # base case
        if i == n - 1:
            res.append(arr[:])
            return

        hm = {}
        for j in range(i, n):
            if arr[j] not in hm:
                hm[arr[j]] = None
                # recursive case
                arr[i], arr[j] = arr[j], arr[i]
                backtrack(i + 1)
                # backtrack case
                arr[i], arr[j] = arr[j], arr[i]
            else:
                continue

    backtrack(0)
    return res


if __name__ == "__main__":
    """
    Empty arrays?
    single element array?
    [[e]]
    [1, 2, 3]
    i = 0
    i = 1
    1 swap 1, 1 swap 2, 1 swap 3 # base when i eq len(array) - 1 # backtrack case swap to original positions 
    [[1, 2, 3] [2, 1, 3] [3, 2, 1] 
    [1, 3, 2] [2, 3, 1] [3, 1, 2]]
     append     append     append
     [1, 2, 3] [2, 1, 3] [3, 2, 1]
    """
    array = [3, 3]
    # array = [1, 2, 3]
    # print(permute_unique(array))
    print(permute_duplicates(array))
