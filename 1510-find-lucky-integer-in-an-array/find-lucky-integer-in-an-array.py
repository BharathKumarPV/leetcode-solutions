class Solution:
    def findLucky(self, arr: list[int]) -> int:
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        ans=-1
        for k,v in freq.items():
            if k==v:
                ans=max(ans,k)
        return ans