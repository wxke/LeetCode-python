字典序排数
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = [str(i) for i in range(1,n+1)]
        nums = sorted(nums)
        res = []
        for i in nums:
            res.append(int(i))
        
        return res
