class Solution:
    def climbStairs(self, n: int) -> int:
        cur,prev=1,1
        for i in range (1,n):
            next=prev+cur
            prev=cur
            cur=next
        return cur
        