class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans=[]
        for i in range(0,len(words)):
            for j in range(0,len(words[i])):
                if words[i][j]==x: 
                    ans.append(i)
                    break
        return ans