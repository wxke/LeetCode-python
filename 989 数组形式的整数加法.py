数组形式的整数加法
class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        s = ''.join(str(i) for i in A)
        s = eval(s)+eval(str(K))
        li = []
        if s == 0:
            return [0]
        while s:
            li.append(s%10)
            s= s//10
        return li[::-1]
