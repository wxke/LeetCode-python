生命游戏
class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        q = copy.deepcopy(board)
        hang = len(board)
        lie = len(board[0])
        for i in range(hang):
            for j in range(lie):
                li = []
                if i-1 >=0:
                    li.append(board[i - 1][j])
                if i-1>=0 and j -1>=0:
                    li.append(board[i - 1][j - 1])
                if i-1>=0 and j +1 < lie:
                    li.append(board[i - 1][j + 1])
                if j -1 >=0:
                    li.append(board[i][j - 1])
                if j +1 <lie:
                    li.append(board[i][j + 1])
                if i+1<hang and j+1 < lie:
                    li.append(board[i + 1][j + 1])
                if i+1<hang and j-1 >=0:
                    li.append(board[i + 1][j - 1])
                if i+1 <hang:
                    li.append(board[i + 1][j])
                cont = li.count(1)
                if cont == 3:
                    q[i][j] = 1
                if cont > 3:
                    q[i][j] = 0
                if cont < 2:
                    q[i][j] = 0
        for i in range(hang):
            for j in range(lie):
                board[i][j] = q[i][j]
