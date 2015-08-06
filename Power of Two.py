class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        counter = 0
        index = 1
        while index < 64:
            if n & 1:
                counter += 1
            n = n >> 1
            index += 1
        if counter == 1:
            return True
        else:
            return False