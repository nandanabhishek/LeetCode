class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        
        increase = True
        decrease = True
        
        for i in range(len(A)-1):
            
            if A[i] > A[i+1]:
                increase = False
                
            if A[i] < A[i+1]:
                decrease = False
                
        return increase or decrease
        
