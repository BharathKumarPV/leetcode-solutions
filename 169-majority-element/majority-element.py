class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count=0
        for i in nums:
               if count==0:
                   ele=i
               if ele == i:
                     count+=1
               else:
                    count-=1
        return ele
        