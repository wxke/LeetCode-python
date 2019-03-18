有效的数独
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            row = []
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    row.append(board[i][j])
            # print("----",row)
            if len(row) != len(list(set(row))):
                return False
        
        
        for i in range(len(board[0])):
            row = []
            for j in range(len(board)):
                if board[j][i] != ".":
                    row.append(board[j][i])
            # print("++++",row)
            if len(row) != len(list(set(row))):
                return False
        
        for i in range(0,len(board),3):
            for j in range(0,len(board[0]),3):
                row = []
                if board[i][j] !='.':
                    row.append(board[i][j])
                if board[i][j+1] !='.':
                    row.append(board[i][j+1])
                if board[i][j+2] !='.':
                    row.append(board[i][j+2])
                if board[i+1][j] !='.':
                    row.append(board[i+1][j])
                if board[i+1][j+1] !='.':
                    row.append(board[i+1][j+1])
                if board[i+1][j+2] !='.':
                    row.append(board[i+1][j+2])
                if board[i+2][j] !='.':
                    row.append(board[i+2][j])
                if board[i+2][j+1] !='.':
                    row.append(board[i+2][j+1])
                if board[i+2][j+2] !='.':
                    row.append(board[i+2][j+2])
                # print("----",row)
                if len(row) != len(list(set(row))):
                    return False
        return True
