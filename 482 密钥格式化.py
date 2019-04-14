密钥格式化
class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = S.replace("-","")
        if s == "":
            return ""
        if len(s) == 1:
            return s.upper()
        lis = []
        for i in range(len(s),0,-K):
            lis.append(s[i-K:i])
        if i !=K:
            lis.append(s[:i])
        lis = lis[::-1]
        s = ""
        for i in lis:
            if i:
                s += i +"-"
        return s[:-1].upper()
