class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      l=0
      r=0
      buy=0
      max_profit=0
      while r<len(prices):
        if prices[r]-prices[l]<0:
            l=r
            r+=1
        else:
            max_profit+=(prices[r]-prices[l])    
            l=r
            r+=1
      return max_profit