class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = prices[0]
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            else:
                maxprofit = max(maxprofit, prices[i] - minprice)
        return maxprofit
t = Solution()
print(t.maxProfit([7,6,5,3,2,1]))