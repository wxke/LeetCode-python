亲密字符串
class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A ==B:
            q =set(A)
            for i in q:
                if A.count(i) >=2:
                    return True
            return False
        dic = zip(A,B)
        dic = dict(dic)
        flag = 0
        a_list =[]
        b_list =[]
        for i,j in dic.items():
            if i != j:
                flag +=1
                a_list.append(i)
                b_list.append(j)
        if flag == 2 and a_list == b_list[::-1]:
            return True
        else:
            return False

