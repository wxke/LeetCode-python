强整数
class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        x_list = []
        y_list = []
        s = []
        for i in range(64):
            a = x**i
            if a > bound:
                break
            x_list.append(a)
        for i in range(64):
            a = y**i
            if a > bound:
                break
            y_list.append(a)
            
        for i in range(bound+1):
            
            for j in x_list:
                if j > i :
                    break
                if i - j in y_list:
                    s.append(i)
                    break
        return s
            
