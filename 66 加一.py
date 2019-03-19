加一
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ""
        for i in digits:
            s += str(i)
        s = int(s) +1
        list1 = []
        while s:
            list1.append(s%10)
            s = s // 10
        return list1[::-1]
