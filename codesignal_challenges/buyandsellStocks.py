"""
You are given the prices of a stock, in the form of an array of integers, prices. 
Let's say that prices[i] is the price of the stock on the ith day (0-based index). 
The ith day is important for conceptual understanding. 
Assuming that you are allowed to buy and sell the stock only once, 
your task is to find the maximum possible profit (the difference between the buy and sell prices).

Note: You can assume there are no fees associated with buying or selling the stock.

Example

For prices = [6, 3, 1, 2, 5, 4], the output should be buyAndSellStock(prices) = 4.

It would be most profitable to buy the stock on day 2 and sell it on day 4. 
Thus, the maximum profit is prices[4] - prices[2] = 5 - 1 = 4.

For prices = [8, 5, 3, 1], the output should be buyAndSellStock(prices) = 0.

Since the value of the stock drops each day, there's no way to make a profit from selling it. 
Hence, the maximum profit is 0.

For prices = [3, 100, 1, 97], the output should be buyAndSellStock(prices) = 97.

It would be most profitable to buy the stock on day 0 and sell it on day 1. 
Thus, the maximum profit is prices[1] - prices[0] = 100 - 3 = 97.
"""


def buyAndSellStock(prices):
    # input: an array of prices given on an ith day
    mx, cur = 0, 0 
    for price in reversed(prices):                       
        cur = max(cur, price)
        print("cur, price", cur, price)  # visualize under the hood    
        pot = cur - price
        print("pot", pot)                # visualize under the hood    
        mx = max(pot, mx)
        print("mx", mx)                  # visualize under the hood    
    # output: maximum profit
    return mx

if __name__ == "__main__":
    # stock_prices = [3, 100, 1, 97]
    stock_prices = [10, 30, 7, 15, 30, 1] 
    print(buyAndSellStock(stock_prices))
    """
    This function take an array of stocks and each index represents an ith day.
    As it traverses through the stock prices, looking for the difference
    between the ith day and the ith day prior, it is looking for values that
    are less than the current for MAX profitablility else pot and mx are 0.
    When pot and mx are 0 the function will move on the the ith position (reversed).
    Since, the function is looking for the max it will return the max difference. 
    """