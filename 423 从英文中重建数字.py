从英文中重建数字
class Solution:
    def originalDigits(self, s: str) -> str:     
        dic1 = {
            "z":["zero",0],
            "w":["two",2],
            "u":["four",4],
            "x":["six",6],
            "g":["eight",8]   
        }
        dic2 = {
            "o":["one",1],
            "h":["three",3],
            "f":["five",5],
            "s":["seven",7],
        }
        dic3 = {
            "i":["nine",9]
        }
        str1 = ""
        for k in dic1:
            if k in s:
                cot = s.count(k)
                for j in dic1[k][0]:
                    s = s.replace(j,"",cot)
                
                str1 += str(dic1[k][1]) * cot
        
        for k in dic2:
            if k in s:
                cot = s.count(k)
                for j in dic2[k][0]:
                    s = s.replace(j,"",cot)
                
                str1 += str(dic2[k][1]) * cot
        for k in dic3:
            if k in s:
                cot = s.count(k)
                for j in dic3[k][0]:
                    s = s.replace(j,"",cot)
                
                str1 += str(dic3[k][1]) * cot
                
        return "".join(sorted(str1))
