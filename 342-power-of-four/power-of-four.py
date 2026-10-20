class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        count=0
        while (n&1)==0:
            n>>=1
            count+=1
        if n==1  and count % 2==0:
            return True
        return False
        
            