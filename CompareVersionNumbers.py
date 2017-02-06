class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        if len(v1) <= len(v2):
            self.add_zero(v1, v2)
        else:
            self.add_zero(v2, v1)
        return self.compare(v1, v2)

    # len(v2)>len(v1)
    def add_zero(self, v1, v2):
        l1 = len(v1)
        l2 = len(v2)
        for i in range(l1, l2):
            v1.append('0')

    def compare(self, v1, v2):
        if len(v1) >= 1 and int(v1[0]) > int(v2[0]):
            return 1
        elif len(v1) >= 1 and int(v1[0]) < int(v2[0]):
            return -1
        elif len(v1) >= 2:
            n_v1 = v1[1:]
            n_v2 = v2[1:]
            return self.compare(n_v1, n_v2)
        else:
            return 0

if __name__ == '__main__':
    s = Solution()
    print(s.compareVersion('1.1', '1'))
