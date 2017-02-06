#-*-coding:utf-8-*-#
# 利用bfs 对搜索到的o点进行 广度搜索,搜索这个点的下和右的o点
# 虽然是 accept了,但是本地运行会报 'str' object does not support item assignment 错误
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def fill(x, y):
            if x < 0 or y < 0 or x >= m or y >= n or board[x][y] == 'D' or board[x][y] == 'X':
                return
            board[x][y] = 'D'
            queue.append((x, y))

        def bfs(x, y):
            if board[x][y] == 'O':
                fill(x, y)
            while queue:
                cur_x, cur_y = queue.pop(0)
                fill(cur_x + 1, cur_y)
                fill(cur_x, cur_y + 1)
                fill(cur_x - 1, cur_y)
                fill(cur_x, cur_y - 1)


        m = len(board)
        if m == 0:
            return None
        n = len(board[0])

        queue = []
        for i in range(n):
            bfs(0, i)
            bfs(m - 1, i)
        for i in range(m):
            bfs(i, 0)
            bfs(i, n - 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'D':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


if __name__ == '__main__':
    s = Solution()
    board = ["XXXX","XOOX","XXOX","XOXX"]
    print(s.solve(board))
