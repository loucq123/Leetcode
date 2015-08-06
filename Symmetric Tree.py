# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            return self.helper(root.left, root.right)
    
    def helper(self, tree1, tree2):
        if tree1 is None and tree2 is None:
            return True
        elif tree1 is None or tree2 is None:  # the case one tree is None
            return False
        elif tree1.val != tree2.val:
            return False
        else:
            return self.helper(tree1.left, tree2.right) and self.helper(tree1.right, tree2.left)