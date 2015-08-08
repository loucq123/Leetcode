class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        return self.generateHelper([], n)
        
    def generateHelper(self, solution, n):
        if len(solution) == 2 * n:
            return [''.join(solution)]
        else:
            ans = []
            for newParen in ['(', ')']:
                if not self.judge(solution, newParen, n):
                    continue
                newSolution = solution[:]
                newSolution.append(newParen)
                ans = ans + self.generateHelper(newSolution, n)
            return ans
    
    def judge(self, solution, newParen, size):
        leftParenNumbers = self.countLeftParen(solution)
        rightParenNumbers = len(solution) - leftParenNumbers
        if newParen == '(':
            if leftParenNumbers + 1 > size:
                return False
        else:
            if rightParenNumbers + 1 > leftParenNumbers:
                return False
        return True
        
    def countLeftParen(self, parens):
        leftParenNumbers = 0
        for p in parens:
            if p == '(':
                leftParenNumbers += 1
        return leftParenNumbers