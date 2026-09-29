class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence = sentence.lower()
        for i in range(26):
            ch=chr(97+i)
            if ch not in sentence:
                return False
        return True 