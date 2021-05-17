# Approach-1 :

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
    
    
    
    # time complexity : O(n logn)
    # space complexity : O(1)
    
    
 
# Approach-2 :

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = nums[0], 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate, count = num, 1
            else:
                count -= 1
        return candidate
      
      
      # time complexity : O(n)
      # space complexity : O(1)
      
