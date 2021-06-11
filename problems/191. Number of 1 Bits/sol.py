class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=[]
        while n:
            ans.append(n%2)
            n=n//2
        return ans.count(1)
            
        
