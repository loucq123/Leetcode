class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        return self.combineHelper([], range(1, n + 1), k)
        
    def combineHelper(self, solution, selectedSet, size):
        if len(solution) == size:
            return [solution]
        else:
            ans = []
            for newVector in selectedSet:
                if not self.judge(solution, newVector):
                    continue
                newSolution = solution[:]
                newSolution.append(newVector)
                ans += self.combineHelper(newSolution, selectedSet, size)
            return ans
        
    def judge(self, solution, newVector):
        if len(solution) == 0:
            return True
        if solution[len(solution) - 1] < newVector:
            return True
        else:
            return False