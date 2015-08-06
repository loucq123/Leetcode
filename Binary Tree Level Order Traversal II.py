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
    

class Stack:
    
    def __init__(self):
        self.top = None
        
    def push(self, x):
        node = Node(x)
        node.next = self.top
        self.top = node
        
    def empty(self):
        return self.top is None
        
    def pop(self):
        if self.empty():
            raise Exception('Can not pop an empty stack')
        value = self.top.value
        self.top = self.top.next
        return value
    
    def peek(self):
        if self.empty():
            raise Exception('The stack is empty')
        return self.top


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
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        if root is None:
            return []
        node_queue = Queue()
        value_stack = Stack()
        node_queue.enqueue(root)
        while not node_queue.empty():
             new_queue = Queue()
             result = []
             while not node_queue.empty():
                node = node_queue.dequeue()
                result.append(node.val)
                if node.left is not None:
                    new_queue.enqueue(node.left)
                if node.right is not None:
                    new_queue.enqueue(node.right)
             node_queue = new_queue
             if len(result) > 0:
                 value_stack.push(result)
        
        ans = []
        while not value_stack.empty():
            ans.append(value_stack.pop())
        return ans