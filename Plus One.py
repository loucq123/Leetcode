class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        length = len(digits)
        flag = True
        for d in range(length - 1, -1, -1):
            if 0 <= digits[d] <= 8:
                digits[d] += 1
                flag = False
                break
            if flag and digits[d] == 9:
                digits[d] = 0
        if flag:
            return [1] + digits
        else:
            return digits