class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[start] = nums[start], nums[i]
                start += 1
                
        return start