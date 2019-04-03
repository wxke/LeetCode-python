汇总区间
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        
        start = nums[0]
        end = nums[0]
        res = []
        for i in range(1,len(nums)):
            if nums[i] != end+1:
                if start != end:
                    res.append(str(start)+"->"+str(end))
                else:
                    res.append(str(end))
                start = nums[i]
                end = nums[i]
            else:
                end = nums[i]
        
        if start != end:
            res.append(str(start)+"->"+str(end))
        else:
            res.append(str(end))

                
        return res
