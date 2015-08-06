# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        level = root
        newLevel = None
        newLevelMove = None
        while level is not None:
            if level.left:
                if newLevel is None:
                    newLevel, newLevelMove = level.left, level.left
                else:
                    newLevelMove.next = level.left
                    newLevelMove = newLevelMove.next
            if level.right:
                if newLevel is None:
                    newLevel, newLevelMove = level.right, level.right
                else:
                    newLevelMove.next = level.right
                    newLevelMove = newLevelMove.next
            level = level.next
            if level is None:
                level = newLevel
                newLevel, newLevelMove = None, None