class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = prices[0]
        max = 0

        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            else:
                profit = prices[i] - min
                if profit > max:
                    max = profit
            
        return max

