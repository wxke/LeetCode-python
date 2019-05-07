特殊等价字符串组
class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        list2 = []
        for i in range(len(A)):
            list1 =[]
            s1=''
            s2 = ''
            for j in range(len(A[i])):
                if j%2 ==0:
                    s1 = A[i][j] + s1
                else:
                    s2 = A[i][j] + s2
                
            list1.append("".join((lambda x:(x.sort(),x)[1])(list(s1))))
            list1.append("".join((lambda x:(x.sort(),x)[1])(list(s2))))
            list2.append(list1)
            
        sum1 = 0
        b =[]
        for i in range(len(list2)):
            if list2[i] not in b:
                b.append(list2[i])
        return len(b)
