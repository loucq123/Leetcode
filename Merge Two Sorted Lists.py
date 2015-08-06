# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            tree_node = ListNode(None)
            if l1.val > l2.val:
                tree_node.val = l2.val
                tree_node.next = self.mergeTwoLists(l1, l2.next)
            else:
                tree_node.val = l1.val
                tree_node.next = self.mergeTwoLists(l1.next, l2)
            return tree_node