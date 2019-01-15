# Rotate Array

# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/646/

# Example:
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]

# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]


def rotate(arr, k):
    if len(arr) <= 1:
        return arr

    for i in range(0, k):
        temp = arr[-1]  # last element

        for j in range(len(arr) - 1, 0, -1):
            arr[j] = arr[j - 1]

        arr[0] = temp

    return arr


def test():
    print("passed") if rotate([1, 2, 3, 4, 5, 6, 7],
                              3) == [5, 6, 7, 1, 2, 3, 4] else print("failed")


if __name__ == "__main__":
    test()