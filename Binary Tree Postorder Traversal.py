# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Node:
    def __init__(self, value=None, color='White', next=None):
        self.value = value
        self.color = color
        self.next = next
        
    def getColor(self):
        return self.color
    
    def setColor(self, newColor):
        self.color = newColor
    
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
        

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        if root is None:
            return []
        nodeStack = Stack()
        nodeStack.push(root)
        result = []
        
        while not nodeStack.empty():
            if nodeStack.peek().getColor() == 'Black':
                result.append(nodeStack.pop().val)
                continue
            while nodeStack.peek().getValue().left and nodeStack.peek().getColor() == 'White':
                nodeStack.peek().setColor('Gray')
                nodeStack.push(nodeStack.peek().getValue().left)
            if nodeStack.peek().getColor() == 'White':
                nodeStack.peek().setColor('Gray')
            
            while nodeStack.peek().getValue().right and nodeStack.peek().getColor() == 'Gray':
                nodeStack.peek().setColor('Black')
                nodeStack.push(nodeStack.peek().getValue().right)
            if nodeStack.peek().getColor() == 'Gray':
                nodeStack.peek().setColor('Black')
                
        return result