数组嵌套
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        min1 = 0
        for i in range(len(nums)):
            q = set()
            if nums[i] != -1:
                flag = i
                while True:
                    if nums[i] not in q: 
                        q.add(nums[flag])
                        ind = nums[flag]
                        nums[flag] = -1
                        flag = ind
                    else:
                        break

                min1 = max(min1,len(q))
        
        return min1-1
