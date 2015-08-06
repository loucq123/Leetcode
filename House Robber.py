class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if (len(nums) == 0):
            return 0
        elif (len(nums) == 1):
            return nums[0]
        result = []
        # initialize F(0) = nums[0], F(1) = nums[1]
        result.append(nums[0])
        result.append(max(nums[0], nums[1]))
        for k in range(2, len(nums), 1):
            result.append(max(result[k - 1], result[k - 2] + nums[k]))
        return result[len(nums) - 1]