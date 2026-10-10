class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        n = len(matrix)
        n1 = len(matrix[0])
        result = []
        for j in range(n1):
            row = []
            for i in range(n):
                row.append(matrix[i][j])
            result.append(row)
        return result
                
        