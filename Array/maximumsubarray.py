class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        nowsum = 0
        for n in nums:
            if 0 > nowsum:
                nowsum = 0
            nowsum += n
            result = max(nowsum, result)
        return result