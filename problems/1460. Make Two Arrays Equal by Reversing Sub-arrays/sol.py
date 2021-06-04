# Approach - 1 :

# Time complexity - O(n log n)
# Space Complexity - O(n), as sorted() creates a copy of array


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target)==sorted(arr)
        
        
  
  
  
        
# Approach - 2 :  VVI

# Time complexity - O(n)
# Space complexity - 
