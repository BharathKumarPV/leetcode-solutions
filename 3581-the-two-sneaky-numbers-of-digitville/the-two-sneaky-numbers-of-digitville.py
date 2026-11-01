class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s = set()
        result = []
        for i in range(len(nums)):
            if nums[i] in s:
                result.append(nums[i])
            else:
                s.add(nums[i])
        return result
        