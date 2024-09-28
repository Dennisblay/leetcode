from typing import List


def combination(n: int, k: int) -> List[List[int]]:
    res = []

    def helper(start: int, curr: List[int]):
        if len(curr) == k:
            res.append(curr[:])
            return
        need = k - len(curr)
        for j in range(start, n - (need - 1) + 1):
            curr.append(j)
            helper(j + 1, curr)
            curr.pop()

    helper(1, [])
    return res


if __name__ == "__main__":
    pass
