丑数 II
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        in1 = 0
        in2 = 0
        in3 = 0
        for i in range(n-1):
            res.append(min(res[in1]*2,res[in2]*3,res[in3]*5))
            if res[-1] == res[in1] * 2:
                in1 += 1
            if res[-1] == res[in2] * 3:
                in2 += 1
            if res[-1] == res[in3] * 5:
                in3 += 1
        return res[-1]
