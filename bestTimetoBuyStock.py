
from ast import List


class Solution:
    def bestTimetoBuyStock(self, prices: List[int]) -> int:
        profit = 0
        left = nums[0]
        
        for price in prices:
            left = min(price, left)
            curProfit = price - left
            profit = max(price, curProfit)

        return profit