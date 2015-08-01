class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        answer = 0
        for index in range(32):
            if((n >> index) & 1 == 1):
                answer += 1
        return answer