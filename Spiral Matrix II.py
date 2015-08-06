class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        result = []
        # initialize result
        for r in range(n):
            row = []
            for l in range(n):
                row.append(0)
            result.append(row)
        row, column = 0, -1
        level = n
        number = 0
        
        while level > 0:
            firstDis = level
            middleDis = level - 1
            lastDis = level - 2
            count = 0
            while count < firstDis:
                number += 1
                column += 1
                result[row][column] = number
                count += 1
            count = 0
            while count < middleDis:
                number += 1
                row += 1
                result[row][column] = number
                count += 1
            count = 0
            while count < middleDis:
                number += 1
                column -= 1
                result[row][column] = number
                count += 1
            count = 0
            while count < lastDis:
                number += 1
                row -= 1
                result[row][column] = number
                count += 1
            level -= 2
        return result