# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        elif len(nums) == 2:
            tree_node = TreeNode(nums[0])
            tree_node.right = TreeNode(nums[1])
            return tree_node
        elif len(nums) == 3:
            tree_node = TreeNode(nums[1])
            tree_node.left = TreeNode(nums[0])
            tree_node.right = TreeNode(nums[2])
            return tree_node
        else:
            middle = len(nums) / 2
            tree_node = TreeNode(nums[middle])
            tree_node.left = self.sortedArrayToBST(nums[:middle])
            tree_node.right = self.sortedArrayToBST(nums[middle+1:])
            return tree_node