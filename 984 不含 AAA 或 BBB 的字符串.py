不含 AAA 或 BBB 的字符串
class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        s = ""
        if A >=B:
            while B:
                s = s+"ab"
                A= A-1
                B= B-1
            i= 0
            if A:
                s = s+'a'
                A = A-1
            while A:
                if s[i] == 'a':
                    s = s[:i] +"a"+s[i:]
                    i +=2
                    A = A-1
                else:
                    i +=1
        else:
            while A:
                s = s+"ba"
                A= A-1
                B= B-1
            i= 0
            s = s+'b'
            B = B-1
            while B:
                if s[i] == 'b':
                    s = s[:i] +"b"+s[i:]
                    i +=2
                    B = B-1
                else:
                    i+=1
        return s
