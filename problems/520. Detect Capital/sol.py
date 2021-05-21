class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        ans=[word.upper(), word.lower(), word.title()]
        return word in ans
        
            
        
