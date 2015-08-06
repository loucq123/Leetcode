class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        operationTable = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
        tokenPos = 0
        end = len(s) - 1
        postFixExp = []
        valueStack = []
        opStack = []
        while tokenPos <= end:
            if s[tokenPos] == ' ':
                tokenPos += 1
            elif s[tokenPos] in '0123456789':
                numberEnd = self.readNumber(s, tokenPos)
                postFixExp.append(int(s[tokenPos: numberEnd]))
                tokenPos = numberEnd
            elif s[tokenPos] in '+-':
                if len(opStack) > 0 and opStack[-1] != '(':
                    postFixExp.append(opStack.pop())
                opStack.append(s[tokenPos])
                tokenPos += 1
            elif s[tokenPos] == '(':
                opStack.append('(')
                tokenPos += 1
            elif s[tokenPos] == ')':
                while opStack[-1] != '(':
                    postFixExp.append(opStack.pop())
                opStack.pop()
                tokenPos += 1
            else:
                raise Exception("Unknown character")
                
        while len(opStack) > 0:
            postFixExp.append(opStack.pop())
            
        for exp in postFixExp:
            if type(exp) == int:
                valueStack.append(exp)
            else:
                firstOperand = valueStack.pop()
                secondOperand = valueStack.pop()
                valueStack.append(operationTable[exp](secondOperand, firstOperand))
        return valueStack.pop()

    def readNumber(self, s, start):
        while s[start] in '0123456789':
            start += 1
            if start >= len(s):     # in case of list out of index
                break
        return start