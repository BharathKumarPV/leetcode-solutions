class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result=[]
        maxc=0
        for num in candies:
            if num+extraCandies>=max(candies):
                result.append(True)
            else:
                result.append(False)
        return result