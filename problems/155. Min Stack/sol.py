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
    
    
    
    # Time Complexity: 
                    '''
                    For insert operation: O(1) (As insertion ‘push’ in a stack takes constant time)
                    For delete operation: O(1) (As deletion ‘pop’ in a stack takes constant time)
                    For ‘Get Min’ operation: O(1) (As we have used an auxiliary stack which has it’s top as the minimum element)
                    '''

    # Auxiliary Space: O(n), Use of auxiliary stack for storing values
    
    
    
    
    
    # Approach - 2 :
    
    
            # Time Complexity : O(1), for each operation
            # Space Complexity : O(n) in worst case, but less than O(n) in other cases.
            
            '''
            The above approach can be optimized. We can limit the number of elements in the auxiliary stack.
            We can push only when the incoming element of the main stack is smaller than or equal to the top of the auxiliary stack.
            Similarly during pop, if the pop-off element equal to the top of the auxiliary stack, remove the top element of the auxiliary stack.
            '''
            
            
 class MinStack:

    def __init__(self):
        '''Use two stacks: one to store actual stack elements and the other as an auxiliary stack to store minimum values. The idea is to do push() and pop() operations in such a way that the top of the auxiliary stack is always the minimum
        '''
       
        # initialize your data structure here.
    
        
        

    def push(self, x: int) -> None:
        

        
        
    def pop(self) -> None:
       
      
    
    
    def top(self) -> int:
        

    
    
    def getMin(self) -> int:
        
        
        
        
        

# Approach - 3 : Most optimized

                                # Time complexity : O(1), for each operation
                                # Space complexity : O(1)
            
            
        

