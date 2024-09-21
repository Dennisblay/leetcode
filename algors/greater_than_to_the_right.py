from typing import List


# Write a function that given, an array arr, returns an array containing at each index i
# the amount of numbers that are
# smaller than arr[i] to the right.

def count_greater_than_to_the_right(array: List[int]) -> List[int]:
    array_length: int = len(array)
    res: List[int] = [0] * array_length
    for i in range(array_length):
        current = array[i]
        for j in array[i + 1:]:
            if current > j:
                res[i] += 1
    return res


if __name__ == '__main__':
    # array_input = [5, 4, 3, 2, 1]
    array_input = [1, 2, 0]
    result = count_greater_than_to_the_right(array=array_input)
    print(result)
