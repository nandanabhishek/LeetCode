class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        # the logic is, among n teams only 1 team will won, so n-1 teams will lose
        # hence there will be n-1 match (so that n-1 teams can lose) 
        
        return n-1
            
