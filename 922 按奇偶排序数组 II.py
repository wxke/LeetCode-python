按奇偶排序数组 II
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        list =[]

        for i in range(len(A)):
            if A[i]%2== 0:
                list.append(A[i])
                A[i] =-1
        for  i in range(len(A)):
            if A[i] % 2 ==1 and A[i] != -1:
                list.append(A[i])

        b =[]
        j = len(list)//2
        for i in range(0,len(list)//2):

            b.append(list[i])
            b.append(list[j])
            j=j+1
        return b
