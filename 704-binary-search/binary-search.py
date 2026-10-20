class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n=len(nums)
        low=0
        high=n-1
        while low <= high:
            mid = (low + high)//2
            if target==nums[mid]:
                return mid
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return -1
         
                
        