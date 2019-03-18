整数转罗马数字
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 4: 'IV', 9: 'IX', 40: 'XL', 90: 
            'XC', 400: 'CD', 900: 'CM'}
        list1 =[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        s = ""
        while num:
            for i in range(len(list1)):
                if list1[i] <= num:
                    break
            num = num - list1[i]
            s = s + dic[list1[i]]
            
        return s
            
