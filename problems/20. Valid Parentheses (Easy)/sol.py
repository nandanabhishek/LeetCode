# Approach - 1 : What I thought !!



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
 
        # Traversing the Expression
        for char in s:
            if char in ['(', '{', '[']:
                # Push the element in the stack
                stack.append(char)
            else:

                # IF current character is not opening bracket, then it must be closing.
                # So stack cannot be empty at this point.
                if not stack:
                    return False
                
                current_char = stack.pop()
                if current_char == '(':
                    if char != ")":
                        return False
                if current_char == '{':
                    if char != "}":
                        return False
                if current_char == '[':
                    if char != "]":
                        return False

        # Check Empty Stack
        if not stack: # means valid parenthesis
            return True
        return False
    
    
    # Time complexity : O(n)
    # Space complexity : O(n)
        
        
        
        
       
    
    
# Approach - 2 :



