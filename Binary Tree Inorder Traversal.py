# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        stack = []
        result = []
        left = root
        while left is not None:
            stack.append(left)
            left = left.left
        
        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)
            
            left_of_right_subtree = node.right
            
            while left_of_right_subtree is not None:
                stack.append(left_of_right_subtree)
                left_of_right_subtree = left_of_right_subtree.left
        return result