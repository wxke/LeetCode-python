杨辉三角
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        list = [ [] for i in range(numRows)]
        
        for i in range(len(list)):
            list[i].append(1)
            for j in range(i):
                list[i].append(0)
            list[i][i] =1
        
        if numRows<3:
            return list
        else:
            for i in range(2,numRows):
                for j in range(1,i):
                    list[i][j] = list[i-1][j]+list[i-1][j-1]
        
        
        return list
                    
                
        
