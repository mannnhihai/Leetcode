class Solution:
    def maxProfit(self, prices: list[int]) -> int:
       
        lowestPrice = prices[0]
        maxProfit = 0
        

        for price in prices:

            if price < lowestPrice:
                lowestPrice = price 

            currentProfit = price - lowestPrice

            if currentProfit > maxProfit :
                maxProfit = currentProfit
                
                

        return maxProfit

        
        