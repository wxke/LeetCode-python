自定义字符串排序
class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        import functools
        def dp(a,b):
            if a in S and b in S:
                if S.index(a) < S.index(b):
                    return -1
                elif S.index(a) > S.index(b):
                    return 1
                else:
                    return 0
            elif a not in S:
                return 1
            elif b not in S:
                return -1
            else:
                return 0
        return "".join(sorted(T, key=functools.cmp_to_key(dp)))
        
