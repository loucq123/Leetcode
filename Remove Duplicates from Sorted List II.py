# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
            
        dummy = ListNode(None)
        dummy.next = head
        
        prev = dummy
        middle = dummy.next
        last = dummy.next.next
        prevNumber = None
        
        while last is not None:
            if last.val == middle.val:
                middle = middle.next
                last = last.next
                prevNumber = middle.val
            else:
                if middle.val != prevNumber:
                    prev.next = middle
                    prev = middle
                middle = middle.next
                last = last.next
                
            if last is None:
                if middle.val != prevNumber:
                    prev.next = middle
                    prev = middle
        prev.next = None
                
        return dummy.next