字母大小写全排列
class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        list1 = [S]

        for i in range(len(S)):
            list2 = []
            for s in list1:
                if  s[i].isdigit():
                    list2.append(s)
                else:
                    list2.append(s[0:i]+s[i].upper()+s[i+1:])
                    list2.append(s[0:i]+s[i].lower()+s[i+1:])
            list1 = list2
        return list1
