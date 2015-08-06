# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        lessNumber = self.preTraversal(root.left)
        if lessNumber < k - 1:
            return self.kthSmallest(root.right, k - 1 - lessNumber)
        elif lessNumber == k - 1:
            return root.val
        else:
            return self.kthSmallest(root.left, k)
        
    def preTraversal(self, root):
        if root is None:
            return 0
        lessNumber = self.preTraversal(root.left)
        largeNumber = self.preTraversal(root.right)
        return 1 + lessNumber + largeNumber