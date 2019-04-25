寻找比目标字母大的最小字母
class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        while True:
            target = chr(ord(target) + 1)
            if target > 'z':
                target = 'a'
            if target in letters:
                return target
