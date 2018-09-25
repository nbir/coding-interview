import math


def binary_search(array, value):
    return _binary_search(array, value, 0, len(array) - 1)


def _binary_search(array, value, from_index, to_index):
    if from_index > to_index:
        return None

    mid_index = math.floor((from_index + to_index) / 2)
    mid_value = array[mid_index]

    if value == mid_value:
        return mid_index
    elif value < mid_value:
        return _binary_search(array, value, from_index, mid_index - 1)
    else:
        return _binary_search(array, value, mid_index + 1, to_index)


def test():
    from random import randint

    array = [randint(0, 10000) for i in range(0, 1000)]
    array.sort()

    # Not Found case
    print("passed") if binary_search(array, 10001) == None else print("failed")

    # Found case
    index = randint(0, len(array) - 1)
    value = array[index]

    print("passed") if binary_search(array,
                                     value) == index else print("failed")


if __name__ == "__main__":
    test()
