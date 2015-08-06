class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        if nums == []:
            return [[]]
        elif len(nums) == 1:
            return [nums, []]
        else:
            max_num = max(nums)
            nums.remove(max_num)
            sub = self.subsets(nums)
            subcopy = list(sub)
            for set in sub:
                subcopy.append(set + [max_num])
            return subcopy