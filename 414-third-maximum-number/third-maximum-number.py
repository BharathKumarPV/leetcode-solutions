class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first=float('-inf')
        second=float('-inf')
        third=float('-inf')
        for num in nums:
            if num>first:
                third=second
                second=first
                first=num
            elif num>second and num!= first:
                third=second
                second=num
            elif num>third and num!=second and num!=first:
                third=num
        if third==float('-inf'):
             return first
        else:
            return third
             
       