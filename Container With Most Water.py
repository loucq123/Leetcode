class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        if height is None:
            return 0
        left, right = 0, len(height) - 1
        max_area = 0
        while right > left:
            new_area = min(height[left], height[right]) * (right - left)
            if new_area > max_area:
                max_area = new_area
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area