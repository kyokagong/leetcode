#-*-coding:utf-8-*-#

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        def computeStr(str):
            str_list = list(str)
            str_list.sort()
            return ''.join(str_list)

        keys = [computeStr(str) for str in strs]
        hash = {}
        for i in range(len(strs)):
            if keys[i] not in hash:
                hash[keys[i]] = []
            hash[keys[i]].append(strs[i])
        return [hash[key] for key in hash]