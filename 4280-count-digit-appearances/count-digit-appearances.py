class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count=0
        for num in nums:
            digi=0
            while num>0:
                digi=num%10
                if digi==digit:
                    count+=1
                num=num//10
        return count
        