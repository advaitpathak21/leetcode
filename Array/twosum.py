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
            print(i,n)
            k = target - n
            if k in hamap:
                return hamap[k], i
            hamap[n] = i
        return