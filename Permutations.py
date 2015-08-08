class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        return self.permuteHelper([], nums)
        
    def permuteHelper(self, solution, selectedSet):
        if len(solution) == len(selectedSet):
            return [solution]
        else:
            ans = []
            for newVector in selectedSet:
                if not self.judge(solution, newVector):
                    continue
                newSolution = solution[:]
                newSolution.append(newVector)
                ans += self.permuteHelper(newSolution, selectedSet)
            return ans
        
    def judge(self, solution, newVector):
        if newVector in solution:
            return False
        else:
            return True