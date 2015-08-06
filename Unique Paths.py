class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def __init__(self):
        self.memorization = {}
        
    def uniquePaths(self, m, n):
        if (m, n) in self.memorization.keys():
            return self.memorization[(m, n)]
        if m == 1 or n == 1:
            return 1
        else:
            self.memorization[(m, n)] = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
            return self.memorization[(m, n)]