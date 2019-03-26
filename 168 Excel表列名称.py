Excel表列名称
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        a = ""
        list1 = [chr(i) for i in range(65,91)]
        list1.insert(0,'0')
        while n :
            m = n % 26
            n = n // 26
            # print(m,n)
            if m == 0:
                m = 26
                n = n -1
                
            a = a + list1[m]
            
        return a[::-1]
