区域和检索 - 数组不可变
class NumArray:

    def __init__(self, nums: List[int]):
        self.s = [0]
        sum1 = 0
        for i in nums:
            sum1 += i
            self.s.append(sum1)
        # print(self.s)

    def sumRange(self, i: int, j: int) -> int:
        # print(self.s[j+1] ,self.s[i])
        return self.s[j+1] - self.s[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
