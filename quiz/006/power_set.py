from typing import List


def power_set_recur_duplicates(arr: List[int]) -> List[List[int]]:
    def helper(i: int, subset: List[int]):
        # base condition
        if i == len(arr):
            res.append(subset.copy())
            return
        # Include
        subset.append(arr[i])
        helper(i + 1, subset)
        subset.pop()

        # Exclude
        while i < len(arr) - 1 and arr[i] == arr[i + 1]:
            i += 1
        helper(i + 1, subset)

    res: List[List[int]] = []
    helper(0, [])
    return res


def power_set_recur(arr: List[int]) -> List[List[int]]:
    def helper(i: int, subset: List[int]):
        # base condition
        if i == len(arr):
            res.append(subset.copy())
            return
        # Exclude
        while i < len(arr) - 1 and arr[i] == arr[i + 1]:
            i += 1
        helper(i + 1, subset)
        # Include
        subset.append(arr[i])
        helper(i + 1, subset)
        subset.pop()

    res: List[List[int]] = []
    helper(0, [])
    return res


def power_set_iter(arr: List[int]) -> List[int]:
    # [1, 2, 3] = 2 ^ n  = 3
    res = [[]]
    for i, num in enumerate(arr):
        res += [r + [num] for r in res]

    return res


if __name__ == "__main__":
    array = [1, 8, 7]
    result = power_set_recur(array)
    print(result)
    print(len(result))
