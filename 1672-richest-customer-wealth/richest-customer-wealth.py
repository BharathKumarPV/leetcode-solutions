class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        largest=float('-inf')
        for num in accounts:
            if sum(num)>largest:
                largest=sum(num)
        return largest
        