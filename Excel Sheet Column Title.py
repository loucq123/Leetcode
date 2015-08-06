class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        c = ''
        while n > 0:
            n -= 1
            c = chr(n % 26 + 65) + c
            n = n / 26
        return c