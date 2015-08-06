class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        
        left, right = 0, len(nums) - 1
        middle = left + (right - left) // 2
        while right >= left:
            middle = left + (right - left) // 2
            if target == nums[middle]:
                start, end = middle, middle
                while start >= 1 and nums[start - 1] == target:
                    start -= 1
                while end < len(nums) - 1 and nums[end + 1] == target:
                    end += 1
                return [start, end]
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        return [-1, -1]