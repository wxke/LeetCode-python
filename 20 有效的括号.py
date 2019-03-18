有效的括号
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        lis = []
        for i in s:
            if len(lis) == 0 and (i == ')' or i == "}" or i == "]"):
                return False
            if i == "(" or i == "{" or i == "[":
                lis.append(i)
                continue
            if i == ')' and lis[-1] == '(':
                lis.pop()
                continue
            if i == ']' and lis[-1] == '[':
                lis.pop()
                continue
            if i == '}' and lis[-1] == '{':
                lis.pop()
                continue
            return False
        if lis:
            return False
        else:
            return True
