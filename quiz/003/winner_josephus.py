from typing import List


# T = O(n^2)
def winner_1(n: int, k: int) -> int:
    # arr = list(range(1, n + 1))
    arr = [i + 1 for i in range(n)]  # T, S = O(N)

    def josephus(arr: List[int], start: int) -> int:
        if len(arr) == 1:
            return arr[0]
        index_to_remove = (start + k - 1) % len(arr)
        del arr[index_to_remove]  # T = O(N) (work done by each node)
        return josephus(arr, index_to_remove)

    return josephus(arr, 0)


def winner_2(n: int, k: int) -> int:
    def josephus(n: int) -> int:
        if n == 1:
            return 0
        return (josephus(n - 1) + k) % n

    return josephus(n) + 1


def winner_iterative(n: int, k: int) -> int:
    sp = 0
    for i in range(2, n + 1):
        sp = (sp + k) % i
    return sp + 1


if __name__ == "__main__":
    print(winner_iterative(5, 3))
