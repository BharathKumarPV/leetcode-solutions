class Solution:
    def countEven(self, num: int) -> int:
        count=0
        for i in range(1,num+1):
            digit=0
            while i>0:
                digit+=i%10
                i=i//10
            if digit % 2==0:
                count+=1
        return count
        