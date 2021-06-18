class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findFirst(nums, target):
            
            low = 0
            high = len(nums) - 1
            
            res = -1

            while (low <= high):

                # Normal Binary Search Logic
                mid = (low + high) // 2

                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1

                # If arr[mid] is same as x, we update res and move to the left half.
                else:
                    res = mid
                    high = mid - 1

            return res
            
        def findSecond(nums, target):
            
            low = 0
            high = len(nums) - 1
            
            res = -1

            while(low <= high):

                # Normal Binary Search Logic
                mid = (low + high) // 2

                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1

                # If arr[mid] is same as x, we update res and move to the Right half.
                else:
                    res = mid
                    low = mid + 1

            return res
        
        
        res=2*[-1]
        res[0] = findFirst(nums, target)
        res[1] = findSecond(nums, target)
        
        return res
    
        
        
            
        
