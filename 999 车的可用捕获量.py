车的可用捕获量
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        x,y = 0,0
        for i in range(len(board)):
            if 'R' in board[i]:
                x,y=i,board[i].index('R')
        cout = 0
        for i in range(x,-1,-1):
            if board[i][y] == 'p':
                cout += 1
                break
            if board[i][y] == 'B':
                break
        
        for i in range(x,len(board)):
            if board[i][y] == 'p':
                cout += 1
                break
            if board[i][y] == 'B':
                break
        
        for i in range(y,len(board[0])):
            if board[x][i] == 'p':
                cout += 1
                break
            if board[x][i] == 'B':
                break
        
        for i in range(y,-1,-1):
            if board[x][i] == 'p':
                cout += 1
                break
            if board[x][i] == 'B':
                break
                
        return cout
            
                
        
        
                    
