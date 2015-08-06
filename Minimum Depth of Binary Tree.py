# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def getValue(self):
        return self.value


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, x):
        node = Node(x)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    
    def dequeue(self):
        if self.empty():
            raise Exception('The queue is empty')
        
        val = self.front.getValue()
        self.front = self.front.next
        return val
    
    def empty(self):
        return self.front is None


class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        depth = 0
        if root is None:
            return depth
        node_queue = Queue()
        node_queue.enqueue(root)
        while not node_queue.empty():
            depth += 1
            new_queue = Queue()
            while not node_queue.empty():
                node = node_queue.dequeue()
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    new_queue.enqueue(node.left)
                if node.right:
                    new_queue.enqueue(node.right)
            node_queue = new_queue