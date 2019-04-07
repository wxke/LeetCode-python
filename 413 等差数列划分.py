等差数列划分
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        list1 = []
        len1 = len(A)
        if len1 <= 2:
            return 0
        flag = A[0] - A[1]
        q = []
        for i in range(len1 - 1):
            if A[i] - A[i + 1] == flag:
                q.append(A[i])
            else:
                q.append(A[i])
                if len(q) >= 3:
                    list1.append(q)
                q = []
                q.append(A[i])
                flag = A[i] - A[i + 1]
        if A[-2] - A[-1] == flag:
            q.append(A[-1])
        if len(q) >= 3:
            list1.append(q)
        num = 0
        for i in list1:
            len1 = len(i)
            if len1 == 3:
                num += 1
                continue
            if len1 == 4:
                num +=3
                continue
            flag = 2
            res = 3
            for i in range(len1 - 4):
                flag += 1
                res += flag
            num +=res
        return num
