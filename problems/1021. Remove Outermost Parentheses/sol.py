class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ''  # to store final string
        stack = []
        
        # basket is used to store previous value
        basket = ''
        
        for i in s:
            if i == '(':
                stack.append(i)
            else:
                stack.pop()
            basket += i
            
            # if the stack is empty it means we have a valid
            # decomposition. remove the outer parentheses
            # and put it in the result/res. make sure to
            # clean up the basket though!
            if not stack:
                res += basket[1:-1]
                basket = ''
                
        return res
        
