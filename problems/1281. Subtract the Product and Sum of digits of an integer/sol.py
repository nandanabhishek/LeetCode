# Approach - 1: Most general


sum = 0
        product = 1
        while n>0:
            digit = n%10 #Starts finding digits from right
            sum += digit
            product *= digit
            n = n//10
            
        return product-sum

      
      
      
      
# Approach - 2: Use of string



class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a=str(n)
        sum=0
        product=1
        for i in a:
            sum+=int(i)
            product*=int(i)
        return product-sum
