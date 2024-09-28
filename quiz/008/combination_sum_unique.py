from typing import List


def combination_sum_unique(arr: List[int], target: int) -> List[List[int]]:
    res = []
    n = len(arr)

    arr.sort()

    def helper(start: int, curr: List[int], total=0):
        # base condition(s)
        if total > target:
            return
        if total == target:
            res.append(curr[:])

        hm = {}
        for j in range(start, n):
            if arr[j] not in hm:
                hm[arr[j]] = None
                curr.append(arr[j])
                helper(j + 1, curr, total + arr[j])
                curr.pop()

    helper(0, [], 0)
    return res


if __name__ == "__main__":
    candidates = [1, 2, 2, 2, 5]
    target = 5
    array = [3, 5, 2, 1, 3]
    print(combination_sum_unique(candidates, target))
