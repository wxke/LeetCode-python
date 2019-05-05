柠檬水找零
class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        dic = {5: 0, 10: 0, 20: 0}
        flag = True
        for i in bills:
            if i == 5:
                dic[5] += 1
                continue
            elif i == 10 and dic[5] != 0:
                dic[10] += 1
                dic[5] -= 1
            elif i == 10 and dic[5] == 0:
                flag = False
                break
            elif i == 20:
                if dic[10] ==0 and dic[5]>=3:
                    dic[5] -=3
                    dic[20] +=1
                elif dic[10] !=0 and dic[5] != 0:
                    dic[5] -=1
                    dic[10] -=1
                    dic[20] +=1
                else:
                    flag = False
                    break

        return flag
                
