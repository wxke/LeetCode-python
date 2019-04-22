机器人能否返回原点
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        r = 0
        l = 0
        u = 0
        d = 0
        for i in moves:
            if i == 'R':
                r = r +1
            if i == 'L':
                l = l + 1
            if i == 'U':
                u= u+1
            if i == 'D':
                d = d+1
        if r==l and u==d:
            return True
        else:
            return False
