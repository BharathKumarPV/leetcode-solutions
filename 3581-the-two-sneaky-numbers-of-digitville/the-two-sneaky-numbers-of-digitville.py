class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s = set()
        result = []
        for num in nums:
            if num in s:
                result.append(num)
            else:
                s.add(num)
        return result
        