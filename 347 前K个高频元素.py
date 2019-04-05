前K个高频元素
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = collections.Counter(nums)
        list1 = [(k,v) for k,v in nums.items()]
        list1 = sorted(list1,key=lambda i:i[1])[::-1]
        return [ list1[i][0] for i in range(k)]
