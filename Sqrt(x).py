class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x
        
        left, right = 1, x // 2
        while right >= left:
            middle = left + (right - left) // 2
            middle_square = middle * middle
            if middle_square <= x and (middle + 1) * (middle + 1) > x:
                return middle
            elif middle_square < x:
                left = middle + 1
            else:
                right = middle - 1