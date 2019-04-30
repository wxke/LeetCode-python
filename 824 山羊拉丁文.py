山羊拉丁文
class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        list1 =['a','e','i','o','u','A','E','I','O','U']
        
        list = S.split()
        
        for i in range(len(list)):
            if list[i][0] in list1:
                list[i] += 'ma'
            else:
                first = list[i][0:1]
                list[i] = list[i][1:] + first +"ma"
                
            for j in range(i+1):
                list[i] += 'a'
                
        
        
        s =""
        for i in list:
            s = s +i +' '
            
        s =s[:-1]
        return s
                
            
            
                
        
