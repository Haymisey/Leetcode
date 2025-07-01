class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        max_profit=0
        for p in prices:
            buy=min(buy,p)
            max_profit=max(max_profit,p-buy)
        return max_profit                        