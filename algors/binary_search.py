from timeit import timeit
from typing import List, Union

Number = Union[int, float]


def binary_search(array: List[Union[int, float]], target: Union[int, float]) -> int:
    start: int = 0
    end: int = len(array) - 1

    while start <= end:
        middle: int = start + ((end - start) // 2)  # (end + start) >> 1  # (end + start) // 2
        middle_value = array[middle]

        if target < middle_value:
            end = middle - 1
        elif target > middle_value:  # Use 'elif' to prevent both conditions from running
            start = middle + 1
        else:
            return middle  # Target found

    return -1  # Target not found


def linear_search(array: List[Number], target: Number) -> Number:
    i = 0
    array_length = len(array)
    while i < array_length:
        if array[i] == target:
            return i
        i += 1
    return -1


if __name__ == '__main__':
    # Use timeit to measure execution time for binary_search
    binary_search_time = timeit(
        stmt="binary_search(array, 9900)",
        setup="from __main__ import binary_search; array = list(range(100000))",
        number=1000  # Run it 1000 times for a more stable measurement
    )

    # Use timeit to measure execution time for linear_search
    linear_search_time = timeit(
        stmt="linear_search(array, 9900)",
        setup="from __main__ import linear_search; array = list(range(100000))",
        number=1000  # Run it 1000 times for a more stable measurement
    )

    # Print the results
    print(f"Binary Search Time: {binary_search_time} seconds (for 1000 runs)")
    print(f"Linear Search Time: {linear_search_time} seconds (for 1000 runs)")
