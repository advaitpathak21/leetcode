class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows - 1):
            prev = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(prev[j] + prev[j+1])
            res.append(row)
        return res
