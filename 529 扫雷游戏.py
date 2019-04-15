扫雷游戏
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
            if board[click[0]][click[1]] == 'M':
                board[click[0]][click[1]] = 'X'
                return board
            row = len(board)
            cul = len(board[0])

            def dp(i, j):
                if board[i][j] != 'E':
                    return
                count = 0
                if i - 1 >= 0:
                    if board[i - 1][j] == 'M':
                        count += 1
                if i + 1 < row:
                    if board[i + 1][j] == 'M':
                        count += 1
                if j + 1 < cul:
                    if board[i][j + 1] == 'M':
                        count += 1
                if j - 1 >= 0:
                    if board[i][j - 1] == 'M':
                        count += 1
                if i - 1 >= 0 and j - 1 >= 0 and board[i - 1][j - 1] == 'M':
                    count += 1
                if i - 1 >= 0 and j + 1 < cul and board[i - 1][j + 1] == 'M':
                    count += 1
                if i + 1 < row and j - 1 >= 0 and board[i + 1][j - 1] == 'M':
                    count += 1
                if i + 1 < row and j + 1 < cul and board[i + 1][j + 1] == 'M':
                    count += 1
                if count == 0:
                    board[i][j] = 'B'
                    if i - 1 >= 0:
                        dp(i - 1, j)
                    if i + 1 < row:
                        dp(i + 1, j)
                    if j + 1 < cul:
                        dp(i, j + 1)
                    if j - 1 >= 0:
                        dp(i, j - 1)
                    if i - 1 >= 0 and j - 1 >= 0:
                        dp(i - 1, j - 1)
                    if i - 1 >= 0 and j + 1 < cul:
                        dp(i - 1, j + 1)
                    if i + 1 < row and j - 1 >= 0:
                        dp(i + 1, j - 1)
                    if i + 1 < row and j + 1 < cul:
                        dp(i + 1, j + 1)
                else:
                    board[i][j] = str(count)

            dp(click[0], click[1])
            return board
                
                
                    
        
