# https://www.geeksforgeeks.org/stock-buy-sell/

import math


def brute_force(costs):
    if (len(costs) == 0): return ()

    max_profit_buy_day = -1
    max_profit_sell_day = -1
    max_profit = None

    for buy_day, buy_price in enumerate(costs):
        for sell_day in range(buy_day, len(costs)):
            sell_price = costs[sell_day]
            profit = sell_price - buy_price

            if (max_profit == None or profit > max_profit):
                max_profit_buy_day = buy_day
                max_profit_sell_day = sell_day
                max_profit = profit

    if (max_profit == None): return ()

    return (max_profit_buy_day, max_profit_sell_day)


def max_subarray(costs):
    if len(costs) == 0: return ()
    if len(costs) == 1: return (0, 0)

    # Compute list of daily price change
    price_changes = []
    for i in range(1, len(costs)):
        price_changes.append(costs[i] - costs[i - 1])

    # Find contiguous subarray with largest sum
    (max_from_index, max_to_index, _) = _find_max_subarray(
        price_changes, 0,
        len(price_changes) - 1)

    return (max_from_index, max_to_index + 1)


def _find_max_subarray(array, from_index, to_index):
    # Base case - array of unit length
    if from_index == to_index:
        return (from_index, to_index, array[from_index])

    mid_index = math.floor((from_index + to_index) / 2)

    # Left subarray
    (left_from_index, left_to_index, left_max) = _find_max_subarray(
        array, from_index, mid_index)
    # Right subarray
    (right_from_index, right_to_index, right_max) = _find_max_subarray(
        array, mid_index + 1, to_index)
    # Midpoint crossing subarray
    (cross_from_index,
     cross_to_index, cross_max) = _find_max_crossing_subarray(
         array, from_index, mid_index, to_index)

    if left_max > right_max and left_max > cross_max:
        return (left_from_index, left_to_index, left_max)
    elif right_max > left_max and right_max > cross_max:
        return (right_from_index, right_to_index, right_max)
    else:
        return (cross_from_index, cross_to_index, cross_max)


def _find_max_crossing_subarray(array, from_index, mid_index, to_index):
    left_sum = 0
    left_max = None
    left_max_index = None

    # Find max left sub-subarray including midpoint
    for i in range(mid_index, from_index - 1, -1):
        left_sum += array[i]

        if left_max is None or left_sum > left_max:
            left_max = left_sum
            left_max_index = i

    right_sum = 0
    right_max = None
    right_max_index = None

    # Find max right sub-subarray including midpoint
    for i in range(mid_index + 1, to_index + 1):
        right_sum += array[i]

        if right_max is None or right_sum > right_max:
            right_max = right_sum
            right_max_index = i

    return (left_max_index, right_max_index, left_max + right_max)


def test():
    # Brute force
    print("passed") if brute_force([]) == () else print("failed")
    print("passed") if brute_force([2]) == (0, 0) else print("failed")
    print("passed") if brute_force([10, 11, 7, 10, 6
                                    ]) == (2, 3) else print("failed")
    print("passed") if max_subarray([
        100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90,
        97
    ]) == (7, 11) else print("failed")

    # Maximum subarray
    print("passed") if max_subarray([]) == () else print("failed")
    print("passed") if max_subarray([2]) == (0, 0) else print("failed")
    print("passed") if max_subarray([10, 11, 7, 10, 6
                                     ]) == (2, 3) else print("failed")
    print("passed") if max_subarray([
        100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90,
        97
    ]) == (7, 11) else print("failed")


if __name__ == "__main__":
    test()
