唯一摩尔斯密码词
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        bao = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "
            ---", ".--.","--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        list =[]
        str =""
        for i in words:
            for j in i:
                str= str+bao[ord(j)-ord('a')]

            if str not in list:
                list.append(str)
            str=""
        return len(list)
