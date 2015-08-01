class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        dp = []
        dp.append(0)
        for j in range(1, len(prices), 1):
            F_j = dp[j - 1] + prices[j] - prices[j - 1] if prices[j] > prices[j - 1] else dp[j - 1]
            dp.append(F_j)
        return dp[len(prices) - 1]