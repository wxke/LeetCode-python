相对名次
class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        num =sorted(nums,reverse=True)
        if len(nums) ==1:
            nums[0] = "Gold Medal"
        elif len(nums) == 2:
            nums[nums.index(num[0])] = "Gold Medal"
            nums[nums.index(num[1])] = "Silver Medal"
        elif len(nums) >=3:
            nums[nums.index(num[0])] = "Gold Medal"
            nums[nums.index(num[1])] = "Silver Medal"
            nums[nums.index(num[2])] = "Bronze Medal"
            sum1 = 4
            for i in num[3:]:
                nums[nums.index(i)] = str(sum1)
                sum1 +=1
        return nums
