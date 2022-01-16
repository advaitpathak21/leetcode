class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        if low == high and target == nums[0]: return 0
        
        while high >= low:
            mid = (low + high) // 2
            
            if target == nums[mid]:
                return mid
            
            # left side
            if nums[low] <= nums[mid]:
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                else:
                    high = mid - 1
            # right side
            else:
                if target < nums[mid] or target > nums[high]:
                    high = mid - 1
                else:
                    low = mid + 1

        return -1

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         low = 0
#         high = len(nums) - 1
        
#         if low == high and target == nums[0]: return 0
        
#         while high >= low:
#             mid = (low + high) // 2
#             print(nums[low], nums[mid], nums[high], target)
            
#             if target == nums[mid]:
#                 return mid
            
#             if low == high and target == nums[low]: return low
            
#             # go to right side
#             if nums[mid] > nums[high]: 
#                 print("right side")
#                 if target <= nums[high]:
#                     low = mid + 1
#                 else:
#                     high = mid - 1
                    
#             # go to left side
#             else:
#                 print("left side")    
#                 # print(nums[low], nums[mid], nums[high], target)
#                 if target > nums[mid] or target < nums[l]:
#                     low = mid + 1
#                 else:
#                     high = mid -1
#         return -1