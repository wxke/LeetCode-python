词典中最长的单词
class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words = sorted(words)
        list1 = []
        print(words)
        for i in range(len(words)):
            flag = words[i]
            while True:
                if len(flag) == 1:
                    list1.append(words[i])
                if flag[0:-1] in words:
                    flag =flag[0:-1]
                    continue
                else:
                    break

        long = 0
        a =""
        for i in list1:
            if len(i) > long:
                long = len(i)
                a = i
        return a
