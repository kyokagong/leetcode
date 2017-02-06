#-*-coding:utf-8-*-#
# 每次存一个当前最大值,
# 一次性历遍list, 保存最买入价, 当最低买入价小于第i个值,那么第i个值就是最低买入价
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        profit = 0
        local_profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] - buy > 0:
                local_profit = max(local_profit, prices[i] - buy)
                profit = max(profit, local_profit)
            elif prices[i] - buy < 0:
                buy = prices[i]

        return profit