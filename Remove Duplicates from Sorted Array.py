class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return len(nums)
        free_pointer, move_pointer = 0, 1
        while move_pointer < len(nums):
            if nums[move_pointer] == nums[free_pointer]:
                move_pointer += 1
            else:
                free_pointer += 1
                nums[free_pointer] = nums[move_pointer]
                move_pointer += 1
        return free_pointer + 1