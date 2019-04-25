自除数
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        list=[]
        for i in range(left,right+1):
            q= i
            flag = True
            while(q):
                j = q % 10
                q = q//10
                if j!=0 and i%j==0:
                    continue
                else:
                    flag = False
                    break

            if flag == True:
                list.append(i)


        return list
        
