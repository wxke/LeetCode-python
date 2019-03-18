报数
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "11"
        if n == 1:
            return "1"
        else:
            for i in range(n-2):
                # print(s)
                a = s[0]
                sum1 = 1
                str1 = ""
                for j in range(1, len(s)):
                    if a == s[j]:
                        sum1 += 1
                    else:
                        str1 += str(sum1) + a
                        a = s[j]
                        sum1 = 1
                    if j == len(s) -1 and a == s[j]:
                        str1 += str(sum1) + a
                s = str1

        return s
