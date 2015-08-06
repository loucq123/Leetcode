class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            start = 3
            ans = [[1], [1, 1]]
            prev_row = [1, 1]
            while start <= numRows:
                new_row = [1]
                for i in range(len(prev_row) - 1):
                    new_row.append(prev_row[i] + prev_row[i + 1])
                new_row.append(1)
                ans.append(new_row)
                prev_row = new_row
                start += 1
            return ans