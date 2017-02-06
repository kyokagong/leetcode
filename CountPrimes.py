#-*-coding:utf-8-*-#

"""厄拉多塞筛法
   初始化所有值为prime = True
   从2开始,2的倍数全部都为False
   count += 1
   最后返回count
"""
class Solution(object):
    cache = {}

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime = [True] * n
        count = 0
        for i in range(2,n):
            if isPrime[i]:
                j = i + i
                count += 1
                while j < n:
                    isPrime[j] = False
                    j += i
        return count