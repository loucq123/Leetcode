class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        first_c_has_0, first_r_has_0 = False, False
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    if r == 0:
                        first_r_has_0 = True
                    if c == 0:
                        first_c_has_0 = True
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        row_length = len(matrix)
        column_length = len(matrix[0])
        for r in range(1, row_length):
            if matrix[r][0] == 0:
                for c in range(column_length):
                    matrix[r][c] = 0
        
        for c in range(1, column_length):
            if matrix[0][c] == 0:
                for r in range(row_length):
                    matrix[r][c] = 0
        if first_r_has_0:
            for c in range(column_length):
                matrix[0][c] = 0
        if first_c_has_0:
            for r in range(row_length):
                matrix[r][0] = 0