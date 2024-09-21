from typing import List


def sorted_squared_brute(array: List[int]) -> List[int]:
    array_length = len(array)
    res: List[int] = [0] * array_length
    # O(N)
    for i, x in enumerate(array):
        res[i] = x * x
    res.sort()  # O(NlogN)
    return res


# T, S = O(N)
def sorted_squared_optimized(array: List[int]) -> List[int]:
    # The principle that the greater value has to be from among
    # the first and the last number in the input array.
    array_length = len(array)
    new_array: List[int] = [0] * array_length  # T, S = O(N)
    i: int = 0
    j: int = array_length - 1
    k: int = array_length - 1

    while i <= j:  # O(N)
        sq_i = array[i] ** 2
        sq_j = array[j] ** 2
        if sq_i > sq_j:
            new_array[k] = sq_i
            i += 1
        else:
            new_array[k] = sq_j
            j -= 1
        k -= 1
    return new_array


if __name__ == '__main__':
    input_array = [-9, -6, 2, 6, 2, 20]
    # [ | 81, 4, 4, 36, 400 | ]
    print(sorted_squared_optimized(input_array))
