class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        memorization = {}
        for index in range(len(nums)):
            rest = target - nums[index]
            if rest in memorization:
                restIndex = memorization[rest]
                return [index + 1, restIndex + 1] if restIndex > index else [restIndex + 1, index + 1]
            memorization[nums[index]] = index