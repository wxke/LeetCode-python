最常见的单词
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        a = "!?',;."
        paragraph = paragraph.replace("!"," ").replace("?"," ").replace(","," ").replace(";"," ").replace(".",' '
            ).replace("'"," ")
        paragraph = paragraph.lower()
        paragraph = paragraph.split(" ")
        print(paragraph)
        paragraph = [i for i in paragraph if i not in banned]
        cont = 0
        for i in set(paragraph):
            if i == "":
                continue
            x = paragraph.count(i)
            if x > cont:
                cont = x
                flag = i

        return flag
