# Brute force

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(0, len(nums)):
#             for j in range(i+1, len(nums)):
#                 if ((nums[i]+nums[j])==target):
#                     return i,j


# fast
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hamap = {}
        
        for i, n in enumerate(nums):
            need = target - n
            if need in hamap:
                return hamap[need], i
            hamap[n] = i
        return