class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        memorization = set()
        memorization.add(n)
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in memorization:
                return False
            memorization.add(n)
        return True