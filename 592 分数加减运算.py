分数加减运算
class Solution:
    def fractionAddition(self, expression: str) -> str:
        num1 = []
        num2 = []
        flag = 1
        expression = expression.replace('/',' ')
        expression = expression.replace('+',' ')
        expression = expression.replace('-',' -')
        expression = expression.split(' ')
        flag = 1
        for i in expression:
            if i != '':
                if flag == 1:
                    num1.append(int(i))
                    flag = 2
                else:
                    num2.append(int(i))
                    flag = 1
        print(num1,num2)
        max1 = 1
        for i in set(num2):
            max1 *= i
        for i in range(len(num1)):
            num1[i] *= (max1//num2[i])
        sum1 = sum(num1)
        if sum1 == 0:
            return '0/1'
        elif sum1 == 1 or sum1 == -1:
            return str(sum1)+'/'+str(max1)
        flag =1
        if  sum1 < 0:
            a = -1
            sum1 = sum1 * -1
        else:
            a = 1
        while flag == 1:
            for i in range(2,min(sum1,max1)+1):
                if sum1%i == 0 and max1 % i == 0:
                    flag = 0
                    sum1 = sum1 // i
                    max1 = max1 // i
            if flag == 0:
                flag = 1 
            else:
                flag = 0
            
        return str(a * sum1) + '/' + str(max1)
                        
        
