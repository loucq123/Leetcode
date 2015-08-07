# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        slower, faster = head, head.next.next
        slowerMoveOneStep = False
        while faster is not None:
            if faster.next is None:
                slowerMoveOneStep = True
                break
            slower = slower.next
            faster = faster.next.next
        if slowerMoveOneStep:
            slower = slower.next
        else:
            dummy = ListNode(0)
            slowerNext = slower.next
            slower.next = dummy
            dummy.next = slowerNext
            slower = dummy
        middle = slower
        
        right = middle.next
        prev = middle
        while right is not None:
            rightNext = right.next
            right.next = prev
            prev = right
            right = rightNext
        
        while head is not middle and prev is not middle:
            if head.val == prev.val:
                head = head.next
                prev = prev.next
            else:
                return False
        return True