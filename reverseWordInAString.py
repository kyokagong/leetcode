#-*-coding:utf-8-*-#
# 需要用正则匹配搞掉多余的空字符。。。

import re
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            return None
        p = re.compile(r" +")
        splitS = p.split(s)
        ret = []
        for i in range(len(splitS),0,-1):
            if splitS[i-1] != '':
                ret.append(splitS[i-1])
        return ' '.join(ret)

if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("   a   b "))