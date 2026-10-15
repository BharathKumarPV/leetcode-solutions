class Solution:
    def minElement(self, nums: List[int]) -> int:
        #result=[]
        mini=float('inf')
        for num in nums:
            digit=0
            while num>0:
                digit+=num%10
                num=num//10
            if digit<mini:
                mini=digit
        return mini
   



        