class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        return self.helper([], k, n)
        
    def helper(self, solution, size, target):
        if len(solution) == size and sum(solution) == target:
            return [solution]
        else:
            ans = []
            for newVector in range(1, 10):
                if not self.judge(solution, newVector, target):
                    continue
                newSolution = solution[:]
                newSolution.append(newVector)
                ans += self.helper(newSolution, size, target)
            return ans
    
    def judge(self, solution, newVector, target):
        if len(solution) == 0:
            return True
        
        if solution[-1] >= newVector:
            return False
        else:
            if sum(solution) + newVector > target:
                return False
            return True