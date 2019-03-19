螺旋矩阵 II
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        list1 = [[0 for i in range(n)] for i in range(n)]
        x,j = 0,0
        i = 1
        cont =1
        while cont <= n **2:
            for q in range(x//2  ,n-j//2):
                if list1[x//2][q] == 0:
                    list1[x//2][q] =cont
                    cont +=1
            x += 1

            for q in range(x-x//2,n-x+j):
                if list1[q][n-j//2-1] == 0:
                    list1[q][n-j//2-1] = cont
                    cont +=1
            j += 1

            for q in range(n-j//2-1,j//2 -1 ,-1):
                if list1[n-x//2-1][q] ==0:
                    list1[n-x//2-1][q] = cont
                    cont +=1
            x += 1

            for q in range(n-x//2,x//2 -1,-1): #
                if list1[q][j//2] == 0:
                    list1[q][j//2] = cont
                    cont +=1
            j +=1



        return list1 
