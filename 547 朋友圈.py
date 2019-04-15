朋友圈
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        len1 = len(M)
        a = [i for i in range(0,len1)]
        
        for i in range(0,len(M[0])):
            for j in range(0,len(M)):
                if M[i][j] == 1:
                    if i >= j :
                        for q in range(len1):
                            if a[q] == a[i]:
                                a[q] = a[j]
                    else:
                        for q in range(len1):
                            if a[q] == a[j]:
                                a[q] = a[i]
                    
        print(a)
        ans = dict(collections.Counter(a))
        return len(ans.keys())
