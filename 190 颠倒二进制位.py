颠倒二进制位
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = bin(n)
        n = str(n)[2:]
        if len(n) <32:
            n = "0" *(32-len(n)) +n
        n = n[::-1]
        s = 0
        for i in n:
            s = s*2 + int(i)
        return s
            
