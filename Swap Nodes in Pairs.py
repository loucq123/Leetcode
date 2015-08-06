# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if head is None:
            return None
        elif head.next is None:
            return head
        else:
            rest = head.next.next
            second_node = head.next
            head.next = self.swapPairs(rest)
            second_node.next = head
            return second_node