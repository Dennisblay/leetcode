from typing import List, Union


def power_sum(array: List[Union[int, List]], power=1) -> int:
    sum = 0
    for i in array:
        if type(i) == list:
            sum += power_sum(i, power + 1)
        else:
            sum += i
    return sum ** power


if __name__ == "__main__":
    array: List = [1, 2, [3], [2]]
    print(power_sum(array=array, power=1))
