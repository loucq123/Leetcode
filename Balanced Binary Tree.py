# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        result = self.findDepth(root)
        if result:
            return True
        return False
    
    def findDepth(self, root):
        if root is None:
            return 1
        left_depth = self.findDepth(root.left)
        right_depth = self.findDepth(root.right)
        if left_depth and right_depth:
            if abs(left_depth - right_depth) <= 1:
                return 1 + max(left_depth, right_depth)
            else:
                return False
        else:
            return False