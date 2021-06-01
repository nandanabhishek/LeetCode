class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        n = len(mat)
        mid = n // 2  # bcz when odd length matrix then we need to subtract mid element once, as it was added twice in summation
        
        summation = 0
        
        for i in range(n):
            # primary diagonal
            summation += mat[i][i]
            
            # secondary diagonal
            summation += mat[n-1-i][i]    
            
        if n % 2 == 1:  # odd length matrix
            # remove center element (repeated) on odd side-length case
            summation -= mat[mid][mid]  
            
        return summation   
