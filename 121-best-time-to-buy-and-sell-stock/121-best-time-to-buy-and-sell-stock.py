class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Intuition: Track the minimum price seen so far and calculate profit 
        at each price. Update maximum profit whenever a larger profit is found.
        Return the maximum profit, or 0 if no profit is possible.
        '''
      
        min_buy_sofar = float('infinity')
        max_profit_sofar = float('-infinity')

        for price in prices:
            if price < min_buy_sofar:
                min_buy_sofar = price
            
            current_profit = price - min_buy_sofar
            if current_profit >  max_profit_sofar:
                max_profit_sofar = current_profit

        return max(0, max_profit_sofar)
