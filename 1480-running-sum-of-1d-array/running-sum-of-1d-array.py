class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum=0
        l=[]
        for num in nums:
                sum+=num
                l.append(sum)
        return l