独特的电子邮件地址
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        em = []
        for i in range(len(emails)):
            flag = True
            s = ""
            for j in range(len(emails[i])):
                if emails[i][j] == '.' and flag:
                    continue
                elif emails[i][j] == "@":
                    flag = False
                    s = s + emails[i][j]
                else:
                    s = s + emails[i][j]
            em.append(s)

        list = []
        for i in range(len(em)):
            s=""
            flag = True
            for j in range(len(em[i])):
                if em[i][j] =='+':
                    flag = False
                    continue
                elif em[i][j] == "@":
                    flag = True
                if flag:
                    s = s +em[i][j]



            if s not in list:
                list.append(s)
            
        return len(list)



