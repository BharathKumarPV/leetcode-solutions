class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        largest=float('-inf')
        second_largest=float('-inf')
        mini=float('inf')
        mini2=float('inf')
        for num in nums:
            if num>largest:
                second_largest=largest 
                largest=num
            elif num>second_largest:
                second_largest=num
        for num in nums:
            if num<mini:
                mini2=mini
                mini=num
            elif num<mini2:
                mini2=num
        return (largest*second_largest)-(mini*mini2)