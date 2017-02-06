#-*-coding:utf-8-*-#
# 利用 xor 的位匹配方法求出一个res, 然后利用循环找到每位上值为1的值后,count+=1, 接着res 右移1位
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x is None or y is None:
            return None

        res = x ^ y
        count = 0
        while res > 0:
            if (res & 1 == 1):
                count += 1
            res >>= 1
        return count