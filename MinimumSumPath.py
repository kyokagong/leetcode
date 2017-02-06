#-*-coding:utf-8-*-#
# 动态规划题
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.cache = {}
        if len(grid) == 0:
            return 0
        return self._DP(grid, len(grid)-1, len(grid[0])-1)

    def _DP(self, grid, i, j):
        if (i,j) in self.cache:
            return self.cache[(i,j)]
        if i == 0 and j == 0:
            self.cache[(0,0)] = grid[0][0]
        elif i == 0:
            self.cache[(i, j)] = self._DP(grid, i, j - 1) + grid[i][j]
        elif j == 0:
            self.cache[(i, j)] = self._DP(grid, i-1, j) + grid[i][j]
        else:
            self.cache[(i , j)] = min(self._DP(grid, i, j - 1), self._DP(grid, i - 1, j)) + grid[i][j]
        return self.cache[(i , j)]

if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
    print(s.minPathSum([[7,2],[6,6],[8,6],[8,7],[5,0],[6,0]]))