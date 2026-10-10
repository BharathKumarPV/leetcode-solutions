class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        count1=0
        count2=0
        for num in nums:
            if num >0:
                count1 += 1
            elif num<0:
                count2 += 1
        return max(count1, count2)
        