# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    '''def preorderTraversal(self, root):
        if root == None:
            return []
        else:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)'''
    
    def preorderTraversal(self, root):
        if root is None:
            return []
        s = MyStack()
        s.push(root)
        ans = [root.val]
        temp_node = root
        while not s.empty():
            while temp_node is not None and temp_node.left is not None:
                ans = ans + [temp_node.left.val]
                s.push(temp_node.left)
                temp_node = temp_node.left

            temp_node = s.pop().right 
            if temp_node is not None:
                s.push(temp_node)
                ans += [temp_node.val]
        return ans
            
                
class Node():
    def __init__(self, val=None):
        self.val = val
        self.next = None            


class MyStack():
            
    def __init__(self):
        self.top = None
    
    def push(self, node_value):
        node = Node(node_value)
        if self.top == None:
            self.top = node
            return
        
        node.next = self.top
        self.top = node
    
    def pop(self):
        if self.top == None:
            raise Exception("The stack is empty")
        pop_node_value = self.top.val
        self.top = self.top.next
        return pop_node_value
    
    def empty(self):
        return self.top == None