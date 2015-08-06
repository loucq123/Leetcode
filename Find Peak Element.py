class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        
        mid = len(nums) // 2
        if nums[mid] >  nums[mid + 1]:
            return self.findPeakElement(nums[:mid + 1])
        else:
            return mid + self.findPeakElement(nums[mid:])