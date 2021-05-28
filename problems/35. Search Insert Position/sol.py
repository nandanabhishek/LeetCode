# Approach - 1: Binary Search : O(log n)  , Good Approach !!! , I also thought like this.



class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # Binary Search technique
        l=0
        r=len(nums)-1
        while l <= r:
            mid=(l+r)//2
            if nums[mid]== target:
                return mid
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return l
                
    
        
      
# Approach - 2: O(n * logn) + O(n) which is O(n * log n)




class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if target in nums:
            return nums.index(target)
        nums.append(target)
        nums.sort()
        return nums.index(target)
                
    
        
