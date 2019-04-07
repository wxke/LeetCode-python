甲板上的战舰
class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        cont = 0 
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 and j == 0 and board[i][j] == 'X':
                    cont +=1
                    continue
                if i == 0 and (board[i][j] == 'X' and board[i][j-1] == '.'):
                    cont +=1
                    continue
                if j == 0 and board[i][j] == 'X' and board[i-1][j] == '.':
                    cont +=1
                    continue
                if board[i][j] == 'X' and (board[i-1][j] == '.' and board[i][j-1] == '.'):
                    cont += 1
                    continue
        return cont
