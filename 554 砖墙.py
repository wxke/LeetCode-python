砖墙
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dic = {}
        for i in wall:
            s = 0
            for j in range(len(i) - 1):
                s += i[j]
                dic[s] = dic.get(s,0) + 1
        if not dic:
            return len(wall)
        return len(wall) - max(dic.values())
