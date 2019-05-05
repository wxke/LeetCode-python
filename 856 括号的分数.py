括号的分数
class Solution:
    def matchParentheses(self,S,left):
        ans = [S[left]]
        right = None
        for i in range(left+1,len(S)):
            if S[i] == "(":
                ans.append(S[i])
            else:
                if len(ans) == 1:
                    right = i
                    break
                else:
                    ans.pop()
        return right
    
    def score(self,S,left,right):
        if left + 1 == right:
            return 1
        else:
            index = self.matchParentheses(S,left)
            if index == right:
                return self.score(S,left+1,right-1) * 2
            else:
                return self.score(S,left,index) + self.score(S,index + 1,right)
        
        
    def scoreOfParentheses(self, S: str) -> int:
        return self.score(S,0,len(S)-1)
        
