罗马数字转整数
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        sum = 0
        str = ''
        for i in range(len(s)):
            str = str + s[i]
            if i != len(s)-1:
                if dict[s[i]] < dict[s[i + 1]]:
                    continue
                else:
                    sum = sum + dict[str]
                    str = ''
            else:
                sum = sum + dict[str]
                str = ''

        return sum
            
        
