class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse=0
        original=x
        while x>0:
            digit=x%10
            reverse=reverse*10+digit 
            x=x//10
        if original==reverse:
            return True 
        return False
        