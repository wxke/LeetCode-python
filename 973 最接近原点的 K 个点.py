最接近原点的 K 个点
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        res = []
        
        for q,i in enumerate(points):
            x = i[0]
            y = i[1]
            z = x**2 + y**2
            res.append((z,q))
        ans = []
        res = sorted(res)
        for i in range(K):
            ans.append(points[res[i][1]])
        
        return ans
            
