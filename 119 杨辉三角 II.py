杨辉三角 II
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowNumber = rowIndex + 1
        ret = []
        for i in range(rowNumber): 
            ret.append([1])
            for j in range(1, i + 1):
                if j == i: 
                    ret[i].append(1) 
                else: 
                    ret[i].append(ret[i - 1][j - 1] + ret[i - 1][j])
        return ret[rowIndex]
                
            
