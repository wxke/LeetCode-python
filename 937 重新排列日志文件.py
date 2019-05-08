重新排列日志文件
class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        nums = []
        strs = []
        for i in logs:
            list1 = i.split(" ")
            if list1[1].isdigit():
                nums.append(i)
            else:
                strs.append(i)
        for i in range(len(strs)-1):
            for j in range(len(strs)-1-i):
                list1 = strs[j].split(" ",1)
                list2 = strs[j+1].split(" ",1)
                if list1[1] > list2[1]:
                    strs[j],strs[j+1] = strs[j+1],strs[j]

        strs.extend(nums)
        return strs
            
