第一个错误的版本
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1 
        right = n
        if isBadVersion(left):
                return left
        while left + 1 < right:
            if isBadVersion( (left+right) // 2) :
                right = (left+right) // 2
                print(1,left,right)
            else:
                left = (left+right) // 2
                print(2,left,right)
            if isBadVersion(left):
                return left
        return right
