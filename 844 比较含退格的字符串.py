比较含退格的字符串
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack_S=[]
        stack_T=[]
        for i in S:
            if i != '#':
                stack_S.append(i)
            else:
                if len(stack_S):
                    stack_S.pop()
        for i in T:
            if i != '#':
                stack_T.append(i)
            else:
                if len(stack_T):
                    stack_T.pop()
        if stack_S == stack_T:
            return True
        else:
            return False
        
