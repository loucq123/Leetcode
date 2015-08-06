class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()
        length = len(nums)
        closest = sum(nums[:3])
        for first in range(length - 2):
            left, right = first + 1, length - 1
            while right > left:
                newClosest = nums[first] + nums[left] + nums[right]
                if abs(closest - target) > abs(newClosest - target):
                    closest = newClosest
                
                if target > newClosest:
                    left += 1
                elif target < newClosest:
                    right -= 1
                else:
                    return newClosest
        return closest