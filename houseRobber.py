#-*-coding:utf-8-*-#
# 动态规划题
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.cache = {}
        return self.dp(len(nums), nums)

    def dp(self, i, nums):
        if i in self.cache:
            return self.cache[i]
        if i == 0:
            return 0
        if i == 1:
            return nums[0]
        if i == 2:
            return max(nums[0], nums[1])
        self.cache[i] = max(self.dp(i - 1, nums), self.dp(i - 2, nums) + nums[i - 1])
        return self.cache[i]

# HouseRobber2, 首位相连的一个数组
# 方法就是分2种情况,1种是有首没尾,一种是有尾没首
class Solution2(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(0, len(nums) - 2, nums), self.helper(1, len(nums) - 1, nums))

    def helper(self, i, j, nums):
        if i == j:
            return nums[i]

        tmpNums = nums[i:j + 1]
        d = [0] * len(tmpNums)
        d[0] = tmpNums[0]
        d[1] = max(tmpNums[0], tmpNums[1])
        for i in range(2, len(tmpNums)):
            d[i] = max(d[i - 1], d[i - 2] + tmpNums[i])
        return d[-1]

if __name__ == '__main__':
    s = Solution2()
    print(s.rob([0,0]))