class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        uniq = []
        for num in nums:
            if nums.count(num)==1:
                uniq.append(num)
        return sum(uniq)
    
    
    # nums.count(num) calculates the number of times num is present in the list nums !!!
            
