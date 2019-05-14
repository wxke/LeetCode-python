区间列表的交集
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        a, b, res, i, j = len(A), len(B), [], 0, 0
        while i < a and j < b:
            left_a, right_a = A[i].start, A[i].end
            left_b, right_b = B[j].start, B[j].end
            if left_a < left_b:
                left = left_b
            else:
                left = left_a
            if right_a < right_b:
                right = right_a
                i += 1
            else:
                right = right_b
                j += 1
            if right >= left:
                res.append(Interval(left, right))
        return res
