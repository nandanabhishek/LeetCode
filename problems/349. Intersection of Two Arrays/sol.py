# Approach-1 : What I thought


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=set(nums1)
        b=set(nums2)
        arr1=list(a)
        arr2=list(b)
        
        uniq=[]
        for i in arr1:
            for j in arr2:
                if i==j:
                    uniq.append(i)
        return uniq
      
      # Time Complexity : O(n^2)
      # Space Complexity : O(unique elements)
      
      
      
 # Approach-2 : Using Intersection of set properties

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
      
      
      
 # Approach-3 : 
