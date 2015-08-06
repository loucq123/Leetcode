class Solution:
    # @param {integer} n
    # @return {integer}
    def __init__(self):
        self.memorization = {}
    
    def numTrees(self, n):
        if n in self.memorization.keys():
            return self.memorization[n]
        elif n == 0 or n == 1:
            self.memorization[n] = 1
            return 1
        else:
            sum = 0
            for i in range(n):
                sum += self.numTrees(i)*self.numTrees(n - 1 - i)
            self.memorization[n] = sum
            return sum