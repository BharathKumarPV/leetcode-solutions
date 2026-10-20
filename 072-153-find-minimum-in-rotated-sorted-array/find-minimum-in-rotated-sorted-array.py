class Solution:
    def findMin(self, nums: list[int]) -> int:
        mini = float('inf')
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid]<=nums[high]:
                mini = min(mini, nums[mid])
                high = mid - 1
            else:
                mini = min(mini, nums[low])
                low = mid + 1
        return mini
        