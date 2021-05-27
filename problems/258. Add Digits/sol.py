# Approach - 1: Most general approach


class Solution:
    def addDigits(self, num: int) -> int:
        # general approach
        sum = 0
     
        while(num > 0 or sum > 9):
            if(num == 0):
                num = sum
                sum = 0

            sum += num % 10
            num = num // 10
        return sum
        
        
        
        
 # Approach - 2 : Use of maths



class Solution:
    def addDigits(self, num: int) -> int:
 
    if num == 0:
        return 0
    if num % 9 == 0:
        return 9
    else:
        return num % 9
