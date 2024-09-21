from typing import List


def is_monotonic(array: List[int]) -> bool:
    array_length = len(array)
    if array_length <= 0:
        return True
    start = array[0]
    last = array[array_length - 1]

    if start < last:
        for i in range(array_length - 1):
            if array[i] > array[i + 1]: return False
    if start > last:
        for i in range(array_length - 1):
            if array[i] < array[i + 1]: return False
    if start == last:
        for i in range(array_length - 1):
            if array[i] != array[i + 1]: return False

    return True


if __name__ == "__main__":
    # array = [1, 2, 3, 4]
    array = [3, 2, 1, 0]
    print(is_monotonic(array))

    # array_length = len(array)
    # if array_length <= 0:
    #     return True
    #
    # increasing = decreasing = True
    #
    # for i in range(1, array_length):
    #     if array[i - 1] < array[i]:
    #         increasing = False
    #     if array[i - 1] > array[i]:
    #         decreasing = False
    # return increasing or decreasing
