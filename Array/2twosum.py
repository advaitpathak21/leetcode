class Solution:
    def twosum(self, nums: list, target: int):
        hashmap = {}
        for i, n in enumerate(nums):
            k = target - n
            if k in hashmap:
                return k, n
            hashmap[n] = i
        return False

x = Solution()
print(x.twosum([10,15,3,7], 17))