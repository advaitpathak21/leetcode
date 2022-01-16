class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        stack = []
        A = A.split()
        for i in (A):
            stack.append(i)
        stack.reverse()
        return " ".join(stack)

x = Solution()
a = "fwbpudnbrozzifml osdt ulc jsx kxorifrhubk ouhsuhf sswz qfho dqmy sn myq igjgip iwfcqq"
print(x.solve(a))