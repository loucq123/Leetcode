class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        ans = 0
        s_len = len(s)
        for i in range(s_len):
            ans = (ord(s[i]) - 64) * 26 ** (s_len - i - 1) + ans
        return ans