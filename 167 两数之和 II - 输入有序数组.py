两数之和 II - 输入有序数组
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        len1 = len(numbers)
        import bisect
        s = set()
        for i in range(0,len1):
            if numbers[i] in s:
                continue
            for j in range(i+1,len1):
                if numbers[i] + numbers[j] == target:
                    return i+1,j+1
            s.add(numbers[i])
        
