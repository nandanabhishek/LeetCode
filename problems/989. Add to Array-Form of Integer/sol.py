# Approach - 1 : What I though


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans=[]
        string_num=''
        for i in num:
            string_num=string_num+str(i)
        for j in str(int(string_num)+k):
            ans.append(int(j))
        return ans
            
        
        
        
        
# Approach - 2 :



