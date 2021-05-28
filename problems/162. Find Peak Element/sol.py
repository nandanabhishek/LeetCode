# Approach - 1 : Time complexity : O(n), Straightforward Approach


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
1. If in the array, the first element is greater than the second or the last element is          greater than the second last, return the respective element and terminate the program.
2. Else traverse the array from the second index to the second last index
   If for an element array[i], it is greater than both its neighbours, 
   i.e., array[i] > array[i-1] and array[i] > array[i+1], then return that element and            terminate.
        
        '''
        
        # when array has only 1 element
        if (len(nums) == 1) :
            return 0  # index of 1st element
        
        n = len(nums)-1  # to store the highest index
        
        # first or last element is peak element
        # elements must be strictly increasing
        if (nums[0] > nums[1]) :
            return 0
        if (nums[-1] > nums[-2]) :
            return n

        # check for every other element
        for i in range(1, n) :

            # check if the neighbors are smaller
            if (nums[i] > nums[i - 1] and nums[i] > nums[i + 1]) : 
                return i
            
            
        # Time Complexity : O(n)
        
        
        
        
        
        
 # Approach - 2 : Time Complexity : O(log n)
