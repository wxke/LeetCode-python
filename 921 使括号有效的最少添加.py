使括号有效的最少添加
class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        list1 = []
        cont = 0
        for i in S:
            if i == "(":
                list1.append(i)
            if i == ")" and len(list1) == 0:
                cont += 1
                continue
            if  list1[-1] == "("and i == ")":
                list1.pop()
            
        return len(list1) + cont
