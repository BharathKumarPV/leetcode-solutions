class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        unique=sum(set(nums))
        dup = sum(nums) - unique
        miss = n*(n+1)//2 - unique
        return [dup,miss]