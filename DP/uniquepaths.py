class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        
        for i in range(m - 1): #we have the last row
            newrow = [1] * n
            for j in range(n - 2, -1, -1):    # since last column of row is always 1
                newrow[j] = newrow[j + 1] + row[j]
            row = newrow                        # next row will use the prev row as reference
        
        return row[0]