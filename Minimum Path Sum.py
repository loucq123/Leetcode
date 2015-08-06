class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        if grid is None:
            return 0
        dp =  grid[:]
        for m in range(len(dp)):
            for n in range(len(dp[0])):
                if m == 0 and n == 0:
                    pass
                elif m == 0 and n > 0:
                    dp[m][n] = dp[m][n - 1] + grid[m][n]
                elif n == 0 and m > 0:
                    dp[m][n] = dp[m - 1][n] + grid[m][n]
                else:
                    dp[m][n] = min(dp[m - 1][n], dp[m][n - 1]) + grid[m][n]
        return dp[len(dp) - 1][len(dp[0]) - 1]