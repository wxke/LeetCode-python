子域名访问计数
class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dict = {}
        for i in range(len(cpdomains)):
            left,right = cpdomains[i].split(" ")
            list = []
            list = right.split(".")

            for j in range(len(list)):
                s = list[j]
                if j != len(list)-1:
                    for q in range(j+1,len(list)):
                        s = s+"."+list[q]
                if s in dict.keys():
                    dict[s] = dict[s] + int(left)
                else:
                    dict[s] = int(left)

        list = []
        s = ""
        for i,j in dict.items():
            s = str(j)+" "+i
            list.append(s)
            s = ""
        
        return list

