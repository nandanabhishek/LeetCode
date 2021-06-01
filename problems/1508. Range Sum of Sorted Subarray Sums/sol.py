# Approach - 1 : Simple and general method - O(n^2) time compleity


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        ans = []
        
        for i in range(len(nums)):
            pre_sum = 0
            for j in range(i,len(nums)):
                pre_sum += nums[j]
                ans.append(pre_sum)
        ans.sort()
        return sum(ans[left-1:right])%(10**9+7)
    
    
    
    
    
    
# Approach -2 : 

                
