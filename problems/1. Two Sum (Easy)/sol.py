class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=[]  # to store the indices of two number whose sum is equal to tagetSum
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    arr.append(i)
                    arr.append(j)
        return arr
