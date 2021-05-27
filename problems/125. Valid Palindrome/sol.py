# Approach - 1:
              # Time complexity : O(n) 
              # space complexity : O(n)+O(n)
    
    
    
    class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=[]
        string=[]
        for i in s.lower():
            if i.isalnum():
                ans.append(i)
                string.append(i)
    
        return string==ans[::-1]
