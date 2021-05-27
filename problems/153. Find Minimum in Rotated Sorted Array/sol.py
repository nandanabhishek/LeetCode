# Approach - 1 : Just for fun


class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        return nums[0]
        
        
        
        
# Approach - 2 : Important



class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary Search
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
                
        return nums[low]
        
