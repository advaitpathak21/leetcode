class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        flag = False
        for i in nums:
            if i in hashset:
                flag = True
                break
            else:
                hashset.add(i)
        return flag

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         flag = False
#         nums.sort()
#         for i in range(0,len(nums)-1):
#             if (nums[i] == nums[i+1]):
#                 flag = True
#                 break
#         return flag