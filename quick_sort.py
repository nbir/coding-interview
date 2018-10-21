def quick_sort(array):
    _quick_sort(array, 0, len(array) - 1)


def _quick_sort(array, from_index, to_index):
    if (from_index >= to_index): return

    pivot_index = partition(array, from_index, to_index)
    _quick_sort(array, from_index, pivot_index - 1)
    _quick_sort(array, pivot_index + 1, to_index)


def partition(array, from_index, to_index):
    pivot = array[to_index]
    i = from_index

    for j in range(from_index, to_index):
        if array[j] < pivot:
            swap(array, i, j)
            i += 1

    swap(array, i, to_index)

    return i


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def test():
    from random import randint

    # Empty array
    empty_array = []
    quick_sort(empty_array)
    print("passed") if empty_array == [] else print("failed")

    # Non-empty array
    array = [randint(0, 10000) for i in range(0, 1000)]
    _array = array[:]

    quick_sort(array)

    print("passed") if array == sorted(_array) else print("failed")


if __name__ == "__main__":
    test()
