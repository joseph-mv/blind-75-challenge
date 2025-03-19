import math
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        You are given an array prices where prices[i] is the price of a given stock on the ith day.
        '''
        min_price=math.inf
        max_profit=0
        for price in prices:
            min_price=min(min_price,price)
            max_profit=max(max_profit,price-min_price)

        return max_profit