字母异位词分组
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list1 = []
        for i in strs:
            list1.append(''.join(sorted(i)))
        list2 = list(set(list1))
        dict1 = {}
        for i in list2:
            dict1[i] = []
        for index,i in enumerate(list1):
            dict1[i].append(strs[index])
        
        list1 = []
        for i in dict1.values():
            list1.append(i)
        return list1
            
            
            
