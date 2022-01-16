class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        self.output = []
        self.count = 0
        
        def diff(listo):
            return abs(int(listo[0]) - int(listo[1]))
        
        def backtrack(i, csum):
            if len(csum) == 2:
                if (diff(csum) == 2) and csum [0] != csum [1]:
                    print("ADDING TO OUTPUT----------")
                    self.output.append(csum)
                csum.pop()
                
            if i == len(nums): return
            csum.append(nums[i])
            backtrack(i + 1, csum)
        
        for k, c in enumerate(nums):
            csum = [c]
            if k + 1 < len(nums):
                print("bc", k + 1, csum)
                backtrack(k + 1, csum)
        
        return (self.output)

x = Solution()
print(x.findPairs([3,1,4,1,5], 2))

# csum = [1, 3]
# output = [[3,1], [2,4]]
# if csum in output:
#     print(True)
# print(False)