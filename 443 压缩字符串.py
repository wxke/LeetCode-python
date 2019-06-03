压缩字符串
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if chars == []:
            return []
        chars.append("!")
        flag = chars[0]
        res = []
        sum1 = 0
        for i in chars:
            if flag == i:
                sum1 += 1
            else:
                res.append(str(flag))
                if sum1 != 1:
                    for j in str(sum1):
                        res.append(j)
                flag = i
                sum1 = 1
        for i in range(len(chars)):
            chars.pop()
        for i in res:
            chars.append(i)

        return len(chars)
