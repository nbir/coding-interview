# Remove Duplicates from Sorted Array

# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/

# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Given nums = [1,1,2],
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# Example 2:
# Given nums = [0,0,1,1,1,2,2,3,3,4],
# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.


def delete_duplicates(arr):
    unique_count = 0
    curr_num = None

    for i in range(0, len(arr)):
        if curr_num == None or arr[i] != curr_num:
            curr_num = arr[i]
            unique_count += 1

    return unique_count


def test():
    print("passed") if delete_duplicates([1, 1, 2]) == 2 else print("failed")
    print("passed") if delete_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4
                                          ]) == 5 else print("failed")


if __name__ == "__main__":
    test()
