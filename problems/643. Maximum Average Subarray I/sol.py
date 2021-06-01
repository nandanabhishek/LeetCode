# Approach - Sliding Window Technique ... !!! VVI
# Benefits: Instead of O(N^2), we can solve a type of problem in O(N)


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # sliding window technique
        
        max_sum = curr_sum = sum(nums[:k])
        # or
        '''
        curr_sum=0
        for i in range(k):
            curr_sum += nums[i]
        
        max_sum = curr_sum
        '''
        
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i-k] 
            max_sum = max(max_sum, curr_sum)
            
        return max_sum / k
        
        
