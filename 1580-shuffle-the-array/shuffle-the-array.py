class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result=[]
        i=0
        j=n
        for i in range(0,len(nums)):
            if i<j and j<len(nums):
                result.append(nums[i])
                result.append(nums[j])
            i+=1
            j+=1
        return result
            

        