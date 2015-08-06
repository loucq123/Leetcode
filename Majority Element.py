class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        return self.partition(nums)
    def partition(self, nums):
        '''assume nums is not empty
           and the majority element always exists.
        '''
        pivot = nums[0]
        less_than_pivot, equal_pivot, large_than_pivot = 0, 1, 0
        left_pointer, right_pointer = 1, len(nums) - 1
        while left_pointer < right_pointer:
            while nums[left_pointer] <= pivot:
                if left_pointer >= right_pointer:
                    break
                
                if nums[left_pointer] == pivot:
                    nums[equal_pivot], nums[left_pointer] = nums[left_pointer], nums[equal_pivot]
                    equal_pivot += 1
                else:
                    less_than_pivot += 1
                left_pointer += 1
            while nums[right_pointer] > pivot:
                if left_pointer >= right_pointer:
                    break
                large_than_pivot += 1
                right_pointer -= 1
            
            if nums[right_pointer] == pivot:
                nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
                nums[equal_pivot], nums[left_pointer] = nums[left_pointer], nums[equal_pivot]
                equal_pivot += 1
                left_pointer += 1
            else:
                if left_pointer == right_pointer:
                    if nums[left_pointer] > pivot:
                        large_than_pivot += 1
                    else:
                        less_than_pivot += 1
                nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
        largest = max(less_than_pivot, equal_pivot, large_than_pivot)
        if largest == equal_pivot:
            return pivot
        elif largest == less_than_pivot:
            return self.partition(nums[equal_pivot: (equal_pivot + less_than_pivot)])
        else:
            return self.partition(nums[(equal_pivot + less_than_pivot):])