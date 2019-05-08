下降路径最小和
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        row = len(A[0])
        res = [[1000 for i in range(row)] for j in range(len(A))]
        for i in range(row):
            res[0][i] = A[0][i]

        for i in range(1,len(A)):
            for j in range(row):
                if j-1 >=0 and j+1 < row:
                    res[i][j] = A[i][j] + min(res[i-1][j-1],res[i-1][j],res[i-1][j+1])
                elif j-1 >=0 and j+1 >= row:
                    res[i][j] = A[i][j] + min(res[i-1][j-1],res[i-1][j])
                elif j-1 < 0 and j+1 <row:
                    res[i][j] = A[i][j] + min(res[i-1][j],res[i-1][j+1])

        return min(res[-1])
