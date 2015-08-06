# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    '''def reverseList(self, head):
        rest = ListNode(None)
        rest.next = head
        rest = rest.next
        tail = None
        while rest:
            newRest = rest.next
            newHead = rest
            newHead.next = tail
            tail = newHead
            rest = newRest
        return tail'''
    
    def reverseList(self, head):
        return self.helper(head, None)
    
    def helper(self, head, newHead):
        if head is None:
            return newHead
        else:
            next = head.next
            head.next = newHead
            return self.helper(next, head)