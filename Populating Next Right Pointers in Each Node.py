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
        if root is None:
            return
        start = root
        while start.left is not None:
            n = start
            while n is not None:
                n.left.next = n.right
                if n.next is not None:
                    n.right.next = n.next.left
                n = n.next
            start = start.left