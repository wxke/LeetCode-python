第N个数字
class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = 9
        h = i * j
        while h < n:
            i += 1
            j *= 10
            h += i * j
        n -= h - i * j
        m = n // i
        k = n % i
        return int(str(10 ** (i - 1) + m - 1)[-1]) if k == 0 else int(str(10 ** (i - 1) + m)[k - 1])
