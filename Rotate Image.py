class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        if matrix is None:
            return 
        length = len(matrix) - 1
        half_length = len(matrix) // 2 if len(matrix) % 2 == 0 else len(matrix) // 2 + 1
        for i in range(half_length):
            for j in range(i, len(matrix[i]) - 1 - i):
                matrix[i][j], matrix[j][length - i], matrix[length - i][length - j], matrix[length - j][i] = \
                matrix[length - j][i], matrix[i][j], matrix[j][length - i], matrix[length - i][length - j]