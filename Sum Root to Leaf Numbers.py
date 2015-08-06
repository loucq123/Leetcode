# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        _, ans = self.helper(root)
        return ans
        
    def helper(self, root):
        if root is None:
            return 0, 0
        elif root.left is None and root.right is None:
            return 1, root.val
        else:
            left_factor, left_ans = self.helper(root.left)
            right_factor, right_ans = self.helper(root.right)
            new_factor = 10 * (left_factor + right_factor)
            return new_factor, root.val * new_factor + left_ans + right_ans