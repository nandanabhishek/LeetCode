class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ## RC ##
        ## APPRAOCH : 2 POINTER ##
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(1) ##

        left = 0
        right = len(nums) - 1
        
        while(left < right):
            if(nums[left] + nums[right] < target):
                left += 1
            if(nums[left] + nums[right] > target):
                right -= 1
            if((nums[left] + nums[right]) == target):
                return [left+1,right+1]
