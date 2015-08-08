class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        return self.helper([], candidates, target)
        
    def helper(self, solution, candidates, target):
        if sum(solution) == target:
            return [solution]
        else:
            ans = []
            for newVector in candidates:
                if not self.judge(solution, newVector, target):
                    continue
                newSolution = solution[:]
                newSolution.append(newVector)
                ans += self.helper(newSolution, candidates, target)
            return ans
    
    def judge(self, solution, newVector, target):
        if len(solution) == 0:
            return True
        
        if solution[-1] > newVector:
            return False
        else:
            if sum(solution) + newVector > target:
                return False
            return True