class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        lp = 0
        total = 0
        for i in range(n):
            if i==0:
                nums[lp] = nums[i]
                lp += 1
                total += 1
            if nums[i] != nums[lp-1]:
                nums[lp] = nums[i]
                lp += 1
                total += 1
        
        return total
