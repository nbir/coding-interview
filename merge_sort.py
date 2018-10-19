import math


def merge_sort(array):
    temp_array = [0] * len(array)
    _merge_sort(array, temp_array, 0, len(array) - 1)


def _merge_sort(array, temp_array, from_index, to_index):
    if (from_index >= to_index): return

    mid_index = math.floor((from_index + to_index) / 2)

    _merge_sort(array, temp_array, from_index, mid_index)
    _merge_sort(array, temp_array, mid_index + 1, to_index)

    merge(array, temp_array, from_index, mid_index, to_index)


def merge(array, temp_array, from_index, mid_index, to_index):
    i = from_index
    j = mid_index + 1
    k = from_index

    # Merge
    while i <= mid_index and j <= to_index:
        if array[i] < array[j]:
            temp_array[k] = array[i]
            i += 1
        else:
            temp_array[k] = array[j]
            j += 1

        k += 1

    # Copy remaining items
    while i <= mid_index:
        temp_array[k] = array[i]
        i += 1
        k += 1

    while j <= to_index:
        temp_array[k] = array[k]
        j += 1
        k += 1

    # Copy content from temp_array to original array
    for l in range(from_index, to_index + 1):
        array[l] = temp_array[l]


def test():
    from random import randint

    # Empty array
    empty_array = []
    merge_sort(empty_array)
    print("passed") if empty_array == [] else print("failed")

    # Non-empty array
    array = [randint(0, 10000) for i in range(0, 1000)]
    _array = array[:]

    merge_sort(array)

    print("passed") if array == sorted(_array) else print("failed")


if __name__ == "__main__":
    test()