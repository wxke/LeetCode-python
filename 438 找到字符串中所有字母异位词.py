找到字符串中所有字母异位词
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        len_p = len(p)
        len_s = len(s)
        if len_s < len_p:
            return []
        p_list = [0] * 26
        s_list = [0] * 26
        for i in range(len_p):
            p_list[ord(p[i]) - 97] += 1
        for i in range(len_p):
            s_list[ord(s[i]) - 97] += 1
        
        list1 = []
        if p_list == s_list:
            list1.append(0)
        for i in range(1,len_s-len_p+1):
            s_list[ord(s[i-1]) - 97] -= 1
            s_list[ord(s[i+len_p-1]) - 97] += 1
            if s_list == p_list:
                list1.append(i)
        return list1
            
