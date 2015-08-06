class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle) == 1:
            return triangle[0][0]
        for row in range(1, len(triangle)):
            triangle[row][0] = triangle[row - 1][0] + triangle[row][0]
            end = len(triangle[row]) - 1
            for column in range(1, end):
                triangle[row][column] = min(triangle[row - 1][column - 1], triangle[row - 1][column]) + triangle[row][column]
            triangle[row][end] = triangle[row - 1][len(triangle[row - 1]) - 1] + triangle[row][end]
        return min(triangle[len(triangle) - 1])