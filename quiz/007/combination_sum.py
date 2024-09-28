from typing import List


def combination_sum(arr: List[int], target):
    res = []

    def helper(start: int, curr: List[int], total=0):
        # base condition
        if total > target:
            return
        if total == target:
            res.append(curr[:])
        for j in range(start, len(arr)):
            curr.append(arr[j])
            # recursive case
            helper(j, curr, total + arr[j])
            # backtrack case
            curr.pop()

    helper(0, [], 0)
    return res


if __name__ == "__main__":
    array = [2, 3, 6, 7]
    print(combination_sum(array, 7))
