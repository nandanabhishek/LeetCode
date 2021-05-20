# Approach-1 : What I thought 


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        a=[i for i in jewels]
        b=[j for j in stones]
        
        for i in a:
            for j in b:
                if i==j:
                    count += 1
        return count
        
        
        # Time Complexity : O(n^2)
        # Space Complexity : O(1)
        
        
        
        
 # Approach-2 : 


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = 0
        jewels = set(J)  # search in a set is instant - O(1)
        for stone in S:
            if stone in jewels:
                counter += 1
        return counter
      
      # Time Complexity : O(n)
      
