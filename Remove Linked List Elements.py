# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        dummy = ListNode(None)
        dummy.next = head
        
        prev = dummy
        start = dummy.next
        while start is not None:
            if start.val == val:
                prev.next = start.next
                start = start.next
            else:
                prev = prev.next
                start = start.next
        return dummy.next