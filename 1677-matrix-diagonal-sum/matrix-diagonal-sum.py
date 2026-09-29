class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n=len(mat)
        sum=0
        if n%2==0:
            for i in range(0,n):
                sum+=mat[i][i]
                sum+=mat[i][n-i-1]
        else:
            for i in range(0,n):
                sum+=mat[i][i]
                sum+=mat[i][n-i-1]
            sum=sum-mat[n//2][n//2]
        return sum
             