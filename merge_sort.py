import math


def merge_sort(array):
    _merge_sort(array, 0, len(array) - 1)


def _merge_sort(array, from_index, to_index):
    if (from_index >= to_index): return

    mid_index = math.floor((from_index + to_index) / 2)

    _merge_sort(array, from_index, mid_index)
    _merge_sort(array, mid_index + 1, to_index)

    merge(array, from_index, mid_index, to_index)


def merge(array, from_index, mid_index, to_index):
    # Copy items into temporary arrays
    left_array = array[from_index:mid_index + 1]
    right_array = array[mid_index + 1:to_index + 1]

    left_index = 0
    right_index = 0
    index = from_index

    # Sorted merge
    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            array[index] = left_array[left_index]
            left_index += 1
        else:
            array[index] = right_array[right_index]
            right_index += 1

        index += 1

    # Copy remaining items
    while left_index < len(left_array):
        array[index] = left_array[left_index]
        left_index += 1
        index += 1

    while right_index < len(right_array):
        array[index] = right_array[right_index]
        right_index += 1
        index += 1


def test():
    from random import randint

    # Empty array
    empty_array = []
    merge_sort(empty_array)
    print("passed") if empty_array == [] else print("failed")

    # Unit length array
    array = [randint(0, 10000)]
    _array = array[:]
    merge_sort(array)
    print("passed") if array == _array else print("failed")

    # Non-empty array
    array = [randint(0, 10000) for i in range(0, 1000)]
    _array = array[:]
    merge_sort(array)
    print("passed") if array == sorted(_array) else print("failed")


if __name__ == "__main__":
    test()
