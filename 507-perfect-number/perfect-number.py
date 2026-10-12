from math import sqrt
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        count=0
        if num <1:
            return False
        for i in range(1,int(sqrt(num)+1)):
            if num%i==0:
                count+=i
                if num//i!=i:
                    count+=num//i
        if count-num==num:
            return True
        else:
            return False
        