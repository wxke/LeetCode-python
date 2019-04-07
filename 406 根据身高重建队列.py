根据身高重建队列
class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if people == []:
            return []
        a = sorted(people,key=lambda i:(i[0],-i[1]),reverse=True)
        res =[a[0]]
        for i in range(1,len(a)):
            res.insert(a[i][1],a[i])
        return res
