class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s=set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False 