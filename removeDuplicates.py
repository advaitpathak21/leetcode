class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 1
        lp = 1
        for i in range(n):
            if nums[i] != nums[lp-1]:
                nums[lp] = nums[i]
                lp += 1
        
        return lp
