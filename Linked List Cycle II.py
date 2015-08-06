# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None or head.next is None or head.next.next is None:
            return None
        rabbit, tortoise = head.next.next, head.next
        while rabbit is not None:
            if rabbit is tortoise:
                break
            if rabbit.next is None:
                return None
            rabbit = rabbit.next.next
            tortoise = tortoise.next
        
        if rabbit is None:
            return None
        tortoise = head
        while True:
            if rabbit is tortoise:
                return rabbit
            rabbit = rabbit.next
            tortoise = tortoise.next