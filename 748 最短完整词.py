最短完整词
class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        wordss = words[:]
        licensePlate = licensePlate.lower()
        max1 = 20
        str1 = ""

        nums = [str(i) for i in range(0,10)]
        nums.append(" ")
        for i in range(len(licensePlate)):
            if licensePlate[i] not in nums:
                str1 += licensePlate[i]

        licensePlate = str1

        for i in range(len(licensePlate)):
            for j in range(len(words)):
                if licensePlate[i] in words[j] and words[j] != "1":
                    words[j] = words[j].replace(licensePlate[i],"",1)
                else :
                    words[j] = "1"
        print(words)
        for i in range(len(words)):
            if words[i] != '1':
                if len(words[i]) < max1:
                    max1 = len(words[i])
                    str1 = wordss[i]
                    
        return str1
