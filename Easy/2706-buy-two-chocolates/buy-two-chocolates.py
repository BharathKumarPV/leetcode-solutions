class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        mini=float('inf')
        second_minj=float('inf')
        for num in prices:
            if num<mini:
                second_mini=mini
                mini=num
            elif num<second_mini:
                second_mini=num
        cost=mini+second_mini
        if cost>money:
            return money 
        return money-cost
                
        
        