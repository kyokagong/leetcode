#-*-coding:utf8-*-#
# 本题用 统计学上的C就可以解决
# 如果 m < n, 那么结果就是 C(m+n-2, m-1)
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 and n == 0:
            return 0
        if m == 1 or n == 1:
            return 1
        if m > n:
            n, m = m, n
        return self._c(m + n - 2, m - 1)

    def _c(self, base, sel):
        dividend = 1
        divisor = 1
        i = 0
        while i < sel:
            dividend *= base - i
            i += 1
        for j in range(1, sel + 1):
            divisor *= j
        return dividend / divisor
