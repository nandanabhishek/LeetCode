# Approach-1 :

class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        return self.fib(n-1)+self.fib(n-2)
        
        
        
        
# Approach-2 :

class Solution:
    def fib(self, n: int) -> int:
        a=0
        b=1
        for i in range(n):
            a=b
            b=b+a
        return a
