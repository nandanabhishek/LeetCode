class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
    
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                count += 1
    
        if count == 0:  
            return True
        if count == 1 and nums[0] >= nums[len(nums)-1]:
            return True
        
        return False
                    
        # count==0 means whole array is sorted or array has every elements same
        # count==1 means array is rotated just once and first element must be greater than or equal to last element
        
        
        
        '''
        Compare all neignbour elements (a,b) in nums,
        the case of a > b can happen at most once.

        Note that the first element and the last element are also connected.

        If all a <= b, A is already sorted.
        If all a <= b but only one a > b, we can rotate and make b the first element.
        In other cases, return false
        '''
