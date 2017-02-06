#-*-coding:utf-8-*-#

# （1）00, [3-9]0：res[i]=0（无法解析，没有可行解析方式）；
# （2）10, 20：res[i]=res[i-2]（只有第二种情况成立）；
# （3）11-19, 21-26：res[i]=res[i-1]+res[i-2]（两种情况都可行）；
# （4）01-09, 27-99：res[i]=res[i-1]（只有第一种情况可行）；
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # s = s.lstrip('0')
        if len(s) == 0 or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1

        res1, res2 = 1, 1
        i = 1
        while i < len(s):
            if (s[i] == '0' and s[i - 1] <= '9' and s[i - 1] >= '3') or s[i - 1] + s[i] == '00':
                res = 0
            elif s[i - 1] + s[i] == '10' or s[i - 1] + s[i] == '20':
                res = res2
            elif (s[i - 1] == '0' and s[i] <= '9') or (s[i - 1] + s[i] > '26'):
                res = res1
            else:
                res = res1 + res2
            res1, res2 = res, res1
            i += 1
        return res
