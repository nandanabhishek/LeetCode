class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits # when the element at first pos i.e at 0th index is also 9, then we insert 1 to the beginning of the list
      
      
      
      # time complexity : O(n)
      # space complexity : O(1)
