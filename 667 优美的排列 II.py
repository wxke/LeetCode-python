优美的排列 II
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        b = [i for i in range(1, n + 1)]
        b[0] = 0
        a =[1]
        flag = 1
        for i in range(k,1,-1):
            if flag:
                b[a[-1] + i -1] = 0
                a.append(a[-1] + i)
                flag = 0
            else:
                b[a[-1] - i - 1] = 0
                a.append(a[-1] - i)
                flag = 1
        for i in b:
            if i != 0:
                a.append(i)

        return a
