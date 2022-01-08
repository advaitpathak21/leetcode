class Solution:
    # @param A : tuple of integers
    # @return an integer
        # A = list(A)
        # A.sort()
        # return A[0]
    def findMin(self, A):
        l = 0
        r = len(A)-1
        while r > l:
            mid = (l+r)//2
            if A[mid] > A[r]:
                l = mid + 1
            else:
                r = mid
        return A[r]

x = Solution()
print(x.findMin((4, 5, 6, 7, 0, 1, 2)))