class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n=len(nums)
        maximum=float("-inf")
        total=0
        for i in range (0,n):
            total+=nums[i]
            maximum=max(maximum,total)
            if total<0:
                total=0
        return maximum 