class Solution():
    def helper(self, arr, n):
        for i in range(n):
            arr[i] += (arr[arr[i]] % n) * n
        
        for i in range(n):
            arr[i] = arr[i] // n
        
        return arr

    def solve(self, arr):
        n = len(arr)
        arr = self.helper(arr, n)
        return arr

x = Solution()
a = [3, 2, 0, 1]
print(x.solve(a))