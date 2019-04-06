随机数索引
class Solution:

    def __init__(self, nums: List[int]):
        self.dic = {}
        for i in range(len(nums)):
            if nums[i] in self.dic:
                self.dic[nums[i]].append(i)
            else:
                self.dic[nums[i]] = [i]

    def pick(self, target: int) -> int:
        import random
        return random.choice(self.dic[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
