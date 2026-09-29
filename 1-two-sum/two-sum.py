class Solution:
    def twoSum(self, nums, target):
        hash_map = {}

        for i in range(0, len(nums)):
            remaining = target - nums[i]

            if remaining in hash_map:
                return [hash_map[remaining], i]

            hash_map[nums[i]] = i