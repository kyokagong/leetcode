#-*-coding:utf-8-*-#

# 由于这个matrix是有顺序的,所以直接变成sorted array,然后用 binary search就可以解决
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False

        sortRow = []
        m = len(matrix)
        n = len(matrix[0])
        start = 1
        end = n * m
        while start <= end:
            mid = int((start + end) / 2)
            x, y = self.sortId2XY(mid, m, n)
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                end = mid - 1
            elif matrix[x][y] < target:
                start = mid + 1
        return False

    # 这里被小坑了一下
    # 注意因为如果一个 5*3的矩阵, id=9的时候,  x y应该是2,2
    # 所以最好的方法就是id变成真实的sorted array id(id -1)然后再求
    def sortId2XY(self, id, m, n):
        y = (id - 1) % n
        x = int((id - 1) / n)
        return (x, y)
