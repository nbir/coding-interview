# Two Sum

# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/546/

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


def brute_force(arr, target):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] + arr[j]) == target:
                return [i, j]

    return None


def hash_map(arr, target):
    rev_index = {}

    for i in range(0, len(arr)):
        value = arr[i]
        rev_index[value] = i

        diff = target - value
        if diff in rev_index:
            return [rev_index[diff], i]

    return None


def test():
    print("passed") if brute_force([2, 7, 11, 15],
                                   9) == [0, 1] else print("failed")

    print("passed") if hash_map([2, 7, 11, 15], 9) == [0, 1
                                                       ] else print("failed")


if __name__ == "__main__":
    test()