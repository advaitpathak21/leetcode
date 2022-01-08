class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0]:
            return False
        rows = len(matrix)
        ind = []
        
        for r in range(rows):
            if target == matrix[r][-1]:
                return True
            elif target < matrix[r][-1]:
                if target in matrix[r]:
                    return True
                return False
            elif target > matrix[r][0]:
                continue