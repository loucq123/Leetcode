# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        if root is None:
            return []
        level = [root]
        view = []
        while len(level) > 0:
            newLevel = []
            for node in level:
                if node.right is not None:
                    newLevel.append(node.right)
                if node.left is not None:
                    newLevel.append(node.left)
            view.append(level[0].val)
            level = newLevel
            
        return view