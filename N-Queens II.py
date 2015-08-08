class Solution:
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        start = []
        return self.helper(start, n)
        
    def helper(self, solution, n):
        if len(solution) == n:
            return 1
        else:
            ans = 0
            for newPlace in range(n):
                if not self.canPlace(solution, newPlace, n):
                    continue
                newSolution = solution[:]
                newSolution.append(newPlace)
                ans += self.helper(newSolution, n)
            return ans
    
    def canPlace(self, currentSolution, newPos, boardSize):
        for i in range(len(currentSolution)):
            if currentSolution[i] == newPos:
                return False
            if abs(i - len(currentSolution)) == abs(currentSolution[i] - newPos):
                return False
        return True