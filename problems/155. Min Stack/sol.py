class MinStack:

    def __init__(self):
        '''Use two stacks: one to store actual stack elements and the other as an auxiliary stack to store minimum values. The idea is to do push() and pop() operations in such a way that the top of the auxiliary stack is always the minimum
        '''
       
        # initialize your data structure here.
    
        self.stack = [] # main stack
        self.min = [] # auxiliary stack
        

    def push(self, x: int) -> None:
        '''1) push x to the first stack (the stack with actual elements) 
2) compare x with the top element of the second stack (the auxiliary stack). Let the top element be y. 
…..a) If x is smaller than y then push x to the auxiliary stack. 
…..b) If x is greater than y then push y to the auxiliary stack.'''
        
        if not self.stack or x < self.min[-1]:
            self.min.append(x)
        else:
            self.min.append(self.min[-1])
        self.stack.append(x)

        
        
    def pop(self) -> None:
        '''1) pop the top element from the auxiliary stack. 
2) pop the top element from the actual stack and return it.
Step 1 is necessary to make sure that the auxiliary stack is also updated for future operations.'''
        self.min.pop()
        self.stack.pop()
      
    
    
    def top(self) -> int:
        return self.stack[-1]

    
    
    def getMin(self) -> int:
        if not self.min:
            return None
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
