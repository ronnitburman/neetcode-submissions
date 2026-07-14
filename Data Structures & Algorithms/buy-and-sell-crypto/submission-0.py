class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        i=0
        j=1
        max_profit=0
        while j<len(prices):
            profit = prices[j]-prices[i]
            if profit<0:
                i=j
                j+=1
            else:
                max_profit=max(profit, max_profit)
                j+=1
        return max_profit

        