翻转矩阵后的得分
class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        flag = True
        hang = len(A)
        lie = len(A[0])
        while flag:
            flag = False
            for i in range(hang):
                if A[i][0] == 0:
                    flag = True
                    for j in range(lie):
                        if A[i][j] == 0:
                            A[i][j] =1
                        else:
                            A[i][j] = 0
            for i in range(lie):
                list1 =[]
                for j in range(hang):
                    list1.append(A[j][i])
                one = list1.count(1)
                zero = list1.count(0)
                if zero > one:
                    flag = True
                    for j in range(hang):
                        if A[j][i] == 0:
                            A[j][i] =1
                        else:
                            A[j][i] = 0
                    break

        cont = 0
        for i in range(hang):
            for j in range(lie):
                A[i][j] = str(A[i][j])
        for i in range(hang):
            cont += int(''.join(A[i]),2)
        return cont

