class Node():
    
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Stack():
    
    def __init__(self, top=None):
        self.top = top
        
    def empty(self):
        return self.top is None
        
    def push(self, x):
        node = Node(x, self.top)
        self.top = node
        
    def pop(self):
        value = self.top.val
        self.top = self.top.next
        return value
        
    def peek(self):
        return self.top
            

class Queue:
    
    # initialize your data structure here
    def __init__(self):
        self.front = None
        self.helper_stack = Stack()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.helper_stack.push(x)
        temp_stack = Stack(self.helper_stack.top)
        self.front = Stack()
        while not temp_stack.empty():
            self.front.push(temp_stack.pop())

    # @return nothing
    def pop(self):
        self.front.pop()
        temp_stack = Stack(self.front.top)
        self.helper_stack = Stack()
        while not temp_stack.empty():
            self.helper_stack.push(temp_stack.pop())
        if self.front.empty():
            self.front = None
    
    # @return an integer
    def peek(self):
        return self.front.peek().val
        
    # @return an boolean
    def empty(self):
        return self.front is None