# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        pointerA, pointerB = headA, headB
        exchangeTimes = 0
        while pointerA is not None and pointerB is not None:
            if pointerA is pointerB:
                return pointerA
            if exchangeTimes > 2:
                return None
            pointerA = pointerA.next
            pointerB = pointerB.next
            if pointerA is None or pointerB is None:
                if pointerA is None:
                    pointerA = headB
                if pointerB is None:
                    pointerB = headA
                exchangeTimes += 1