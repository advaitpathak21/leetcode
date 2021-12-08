class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ac, ar = len(mat[0]), len(mat)     # actual rows and act columns
        t = r*c                            # total elements after given r,c 
        if (t != ac*ar): return mat          
        
        tmp = []
        for i in range(ar):
            for j in range(ac):
                tmp.append(mat[i][j])
                
        res = [[0 for _ in range(c)] for _ in range(r)]
        k = 0
        for i in range(r):
            for j in range(c):
                res[i][j] = tmp[k]
                k += 1
        return res