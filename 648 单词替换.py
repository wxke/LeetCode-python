单词替换
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        dict = set(dict)
        res = ""
        sentence = sentence.split(" ")
        for i in sentence:
            len1 = len(i)
            flag = 1
            if len1 != 1:
                for j in range(len1):
                    if i[:j] in dict:
                        res += i[:j] + " "
                        flag = 0
                        break       
                if flag == 1:
                    res += i + " "
            else:
                res += i + " "
        
        return res.strip()
        
