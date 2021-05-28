# Approach - 1 : O(n)


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        # it is given that only one peak is present, so this is quite simple
        for i in range(len(arr)):
            if arr[i+1] < arr[i]:
                return i
              
              
              
# Approach - 2 : O(logn)



class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        # Binary search technique
        
        low=0
        high=len(arr)-1
        
        # loops forever since there will be always be a peak in the test case:
        while True: 
            mid = (low+high)//2
            
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] < arr[mid] < arr[mid+1]:
                low = mid + 1
            else:
                high = mid - 1
        
        
        
