# https://www.geeksforgeeks.org/stock-buy-sell/


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


def test():
    print("passed") if brute_force([]) == () else print("failed")
    print("passed") if brute_force([2]) == (0, 0) else print("failed")
    print("passed") if brute_force([10, 11, 7, 10, 6
                                    ]) == (2, 3) else print("failed")


if __name__ == "__main__":
    test()
