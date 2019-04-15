键盘行
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        list1 = ['q','w','e','r','t','y','u','i','o','p','Q','W','E','R','T','Y','U','I','O','P']
        list2 = ['a','s','d','f','g','h','j','k','l','A','S','D','F','G','H','J','K','L']
        list3 = ['z','x','c','v','b','n','m','Z','X','C','V','B','N','M',]
        word =[]

        for i in words:
            flag = True
            for j in i:
                if j not in list1:
                    flag = False
            if flag:
                word.append(i)
        for i in words:
            flag = True
            for j in i:
                if j not in list2:
                    flag = False
            if flag:
                word.append(i)

        for i in words:
            flag = True
            for j in i:
                if j not in list3:
                    flag = False
            if flag:
                word.append(i)
                
        return word

