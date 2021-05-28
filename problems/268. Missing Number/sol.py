# Approach-1 : General and Best Approach- By using XOR operation



class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # using XOR operation
        res = 0
        
        for i in range(1, len(nums)+1):
            res = res ^ i
            
        for num in nums:
            res = res ^ num
        return res
    
    
    # very important concept
    
    # Time complexity : O(n)
    # space complexity : O(1)







# Approach-2 : Using Maths, but has certain limitations



class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # mathematical approach
        n = len(nums)
        return n*(n+1)/2 - sum(nums)
    
    # but this methods fails when the missing number is 0
    
    
    # Time complexity : O(n)
    # space complexity : O(1)
    
    
    
    
    
        
