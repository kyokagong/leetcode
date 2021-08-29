# https://leetcode.com/problems/container-with-most-water/submissions/
# https://www.cnblogs.com/grandyang/p/4455109.html
# 思路: i, j指向两头。然后从两头开始计算, 逐渐缩小

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        res = 0
        while (i < j):
            res = max(res, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
