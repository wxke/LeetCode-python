螺旋矩阵 III
class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        flag = 0
        list1 = [[r0, c0]]
        dir_list =[[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        while len(list1) < R*C:
            for x in range(flag // 2 +1):
                c0 += dir_list[flag % 4][0]
                r0 += dir_list[flag % 4][1]
                
                if 0<= r0 < R and 0<= c0 <C:
                    list1.append([r0,c0])

            flag += 1
        return list1
            
         
