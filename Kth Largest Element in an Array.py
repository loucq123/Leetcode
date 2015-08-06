class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        start, end = 0, len(nums)
        if start + 1 >= end:
            return nums[start]
        v = self.partition(nums, start, end)
        while v != k - 1:
            if v > k - 1:
                end = v
                v = self.partition(nums, start, end)
            elif v < k - 1:
                start = v + 1
                v = self.partition(nums, start, end)
        return nums[v]
    
    def partition(self, nums, start, end):   # can not reach end
        if start + 1 >= end:
            return start
        pivot = nums[start]
        left = start + 1
        right = end - 1
        while right > left:
            while nums[left] >= pivot and left < right:
                left += 1
            while nums[right] <= pivot and left < right:
                right -= 1
            if right > left:
                nums[left], nums[right] = nums[right], nums[left]
        
        if nums[left] < pivot:
            left -= 1
        nums[start], nums[left] = nums[left], nums[start]
        return left