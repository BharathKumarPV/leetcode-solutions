class Solution:
    def minElement(self, nums: List[int]) -> int:
        result = []
        for num in nums:
            digit = 0
            while num > 0:
                digit += num % 10
                num = num // 10
            result.append(digit)
        return min(result)