大礼包
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        res = 0
        n = len(price)
        for i in range(n):
            res += price[i] * needs[i]

        for i in special:
            flag = True
            for j in range(n):
                if needs[j] < i[j]:
                    flag = False
            if flag == False:
                continue
            else:
                for j in range(n):
                    needs[j] -= i[j]
                res = min(res,self.shoppingOffers(price,special,needs) + i[-1])
                for j in range(n):
                    needs[j] += i[j]
                
        return res
