验证栈序列
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        
        len_push = len(pushed)
        if len_push <= 2:
            return True
        a = [-1]
        j = 0
        i = 0
        len_pop = len(popped)
        while i < len_pop:
            if a[-1] == popped[i]:
                a.pop()
                i += 1
            elif j > len_push - 1:
                break
            elif a[-1] != popped[i] :
                a.append(pushed[j])
                j += 1
            
            
        
        return len(a) == 1 and a[-1] == -1
                
        
