class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            ans = (((n >> i) & 1) << (31 - i)) | ans
        return ans