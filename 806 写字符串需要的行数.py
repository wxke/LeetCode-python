写字符串需要的行数
class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        sum = 0
        sum1 = 1
        for i in S:
            if sum <=100 and sum + widths[(ord(i)-ord("a"))] <=100:
                sum =sum + widths[(ord(i)-ord("a"))]
                continue
            else:
                sum1 = sum1+1
                sum =widths[(ord(i)-ord("a"))]
        list =[sum1,sum]
        return list
            
