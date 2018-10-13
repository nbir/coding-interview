# https://www.geeksforgeeks.org/leaders-in-an-array/


def brute_force(numbers):
    leaders = []

    for index, curr_num in enumerate(numbers):
        is_leader = True

        for next_num in numbers[index + 1:]:
            if next_num >= curr_num:
                is_leader = False
                break

        if is_leader:
            leaders.append(curr_num)

    return leaders


def reverse_traversal(numbers):
    if len(numbers) == 0:
        return []

    leaders = []

    last_leader = numbers[-1]
    leaders.append(last_leader)

    for index in range(len(numbers) - 1, -1, -1):
        curr_num = numbers[index]

        if curr_num > last_leader:
            last_leader = curr_num
            leaders.append(last_leader)

    return leaders


def test():
    print("passed") if brute_force([]) == [] else print("failed")
    print("passed") if brute_force([2]) == [2] else print("failed")
    print("passed") if brute_force([16, 17, 4, 3, 5, 2
                                    ]) == [17, 5, 2] else print("failed")
    print("passed") if brute_force([1, 2, 3, 4, 0]) == [4, 0
                                                        ] else print("failed")

    print("passed") if reverse_traversal([]) == [] else print("failed")
    print("passed") if reverse_traversal([2]) == [2] else print("failed")
    print("passed") if reverse_traversal(
        [16, 17, 4, 3, 5, 2]) == [17, 5, 2][::-1] else print("failed")
    print("passed") if reverse_traversal(
        [1, 2, 3, 4, 0]) == [4, 0][::-1] else print("failed")


if __name__ == "__main__":
    test()
