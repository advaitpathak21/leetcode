class Solution:
    def helper(self, data, k):
        if k == 0:
            return 1

        s = len(data) - k

        if data[s] == 0:
            return -1
        res = self.helper(data, k-1)
        
        if k >= 2 and int(data[s:s+2]) <=26:
            res += self.helper(data, k - 2)
        # for i in data:
        #     word = chr(int(i) + 96)
        #     print(word)
        #     res.append(word)
        return (res)

    def answer(self, s: int):
        print (self.helper(s, len(s)))
        
x = Solution()
print(x.answer("12345"))