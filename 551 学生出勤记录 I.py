学生出勤记录 I
class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        A = s.count("A")
        if A >=2:
            return False
        else:
            
            for i in range(len(s)-2):
                if s[i] == "L" and s[i+1] == 'L' and s[i+2] == "L":
                    return False
                
        return True
                    
