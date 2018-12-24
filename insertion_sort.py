def insertion_sort(array):
    if len(array) <= 1:
        return array

    for i in range(1, len(array)):
        temp = array[i]

        # Iterate backwards to find desired position
        j = i - 1
        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = temp


def test():
    from random import randint

    # Non-empty array
    empty_array = []
    insertion_sort(empty_array)
    print("passed") if empty_array == [] else print("failed")

    # Unit length array
    array = [randint(0, 10000)]
    _array = array[:]
    insertion_sort(array)
    print("passed") if array == _array else print("failed")

    # Non-empty array
    array = [randint(0, 10000) for i in range(0, 1000)]
    _array = array[:]
    insertion_sort(array)
    print("passed") if array == sorted(_array) else print("failed")


if __name__ == "__main__":
    test()
