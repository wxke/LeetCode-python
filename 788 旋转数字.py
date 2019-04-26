旋转数字
class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        s= ['2','5','6','9']
        l = ['3','4','7']
        flag =False
        sum1 = 0
        for i in range(N+1):
            q = str(i)
            for j in q:
                if j in l:
                    flag = False
                    break
                else:
                    if j in s:
                        flag = True
                        
            if flag:
                sum1 = sum1+1
                flag = False
                    
                
          
            
        
        return sum1
                
                
                
            
