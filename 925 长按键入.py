长按键入
class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        flag = name[0]
        sum1 = 0
        name +="1"
        for i in range(0,len(name)):
            if flag == name[i]:
                sum1 +=1
            else:
                flag1 = typed[0]
                sum2 = 0
                for j in range(len(typed)):
                    if flag1 == typed[j]:
                        sum2 += 1
                    else:
                        break
                if sum1 > sum2 or flag != flag1:
                    return False
                else:
                    typed = typed[j:]
                sum1 = 1
                flag = name[i]
        return True
