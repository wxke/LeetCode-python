验证外星语词典
class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        word = [i for i in words]
        for i in range(len(words)-1):
            if words[i] in words[i+1]:
                words[i] ,words[i+1] = words[i+1] ,words[i]
            elif words[i+1] in words[i]:
                words[i+1] ,words[i] = words[i],words[i+1]
            for j in range(min(len(words[i+1]),len(words[i]))):
                if words[i][j] == words[i+1][j]:
                    continue
                elif order.index(words[i][j]) < order.index(words[i+1][j]):
                    break
                else:
                    if order.index(words[i][j]) > order.index(words[i+1][j]):
                        return False
        if words == word:
            return True
        else:
            return False
