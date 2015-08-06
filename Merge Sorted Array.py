class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        self.helper(nums1, m, 0, nums2, n)
        
    def helper(self, nums1, m, start, nums2, n):
        if n == 0:
            return
        if start == m:
            for i in range(n):
                nums1[start + i] = nums2[i]
            return
        
        if nums1[start] > nums2[0]:
            self.moveOneStepBehind(nums1, start, m)
            nums1[start] = nums2[0]
            start += 1
            m += 1
            n -= 1
            nums2 = nums2[1:]
        else:
            start += 1
        self.helper(nums1, m, start, nums2, n)
            
    def moveOneStepBehind(self, nums, start, end):
        for i in range(end - 1, start - 1, -1):
            nums[i + 1] = nums[i]