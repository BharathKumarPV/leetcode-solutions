class Solution:
    def mirrorDistance(self, n: int) -> int:
        reverse=0
        original=n
        while n>0:
            digit=n%10
            reverse=reverse*10+digit
            n=n//10
        return abs(original-reverse)
            
            
        
        