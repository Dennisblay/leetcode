from typing import List, Union

Number = Union[int, float]

# O(n2)
def insertion_sort(array: List[Number]) -> List[Number]:
    """
    Insertion
    sort is an algorithm to sort the values in an array.
    :return:
    - list: The sorted list of elements.
    """
    array_length: int = len(array)
    i: int = 1
    while i < array_length:
        current_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > current_item:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = current_item
        i = i + 1
    return array


