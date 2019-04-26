逃脱阻碍者
class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        sum1 = abs(target[0])+abs(target[1])
        min1 = sys.maxsize
        for i in ghosts:
            min1 = min(min1,abs(i[0]-target[0])+abs(i[1]-target[1]))
        return min1 > sum1
