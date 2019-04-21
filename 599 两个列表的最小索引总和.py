两个列表的最小索引总和
class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic1 = zip(list1,[i for i in range(len(list1))])
        dic1 = dict(dic1)
        # print(dic1)
        dic2 = zip(list2,[i for i in range(len(list2))])
        dic2 = dict(dic2)
        max1 = sys.maxsize
        a = []
        for i in dic1:
            try:
                if max1 > dic2[i] + dic1[i]:
                    max1 = dic2[i] + dic1[i]
                    a = []
                    a.append(i)
                elif max1 == dic2[i] + dic1[i]:
                    a.append(i)
            except:
                continue
        return a
