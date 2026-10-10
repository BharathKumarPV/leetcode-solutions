class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_price=0
        mp=float("inf")
        n=len(prices)
        for i in range (0,n):
            mp=min(mp,prices[i])
            max_price=max(max_price,prices[i]-mp)
        return max_price
            