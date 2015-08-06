class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        result = []
        left_product = 1
        for i in range(len(nums)):
            result.append(left_product)
            left_product *= nums[i]
        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        return result