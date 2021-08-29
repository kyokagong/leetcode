# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
# https://www.cnblogs.com/grandyang/p/4480780.html
# 思路。 设置一个map默认值是-1, 用于记录字符出现时候的位置。还有一个left,就是当前还没有重复的时候最左侧的位置index。
# 如果有重复, 那么left就变成上次重复的地方。 最大的长度就变成 i - left

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_map = defaultdict(lambda: -1)
        res = 0
        left = -1
        for i in range(len(s)):
            left = max(left, s_map[s[i]])
            s_map[s[i]] = i
            res = max(res, i - left)

        return res


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("dvdf"))
