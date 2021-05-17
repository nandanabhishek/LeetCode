# Approach - 1 : 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False
      
      
      
      # time complexity : O(n log n)
      # space complexity : O(1)
      
      
      
      
# Approach - 2 : Better way - Use of Set concept

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)
