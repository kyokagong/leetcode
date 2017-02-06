#-*-coding:utf-8-*-#
# 一题DP题
# i=0, count[0]=1 //empty tree
#
# i=1, count[1]=1 //one tree
#
# i=2, count[2]=count[0]*count[1] // 0 is root
#             + count[1]*count[0] // 1 is root
#
# i=3, count[3]=count[0]*count[2] // 1 is root
#             + count[1]*count[1] // 2 is root
#             + count[2]*count[0] // 3 is root
#
# i=4, count[4]=count[0]*count[3] // 1 is root
#             + count[1]*count[2] // 2 is root
#             + count[2]*count[1] // 3 is root
#             + count[3]*count[0] // 4 is root
# ..
# ..
# ..
#
# i=n, count[n] = sum(count[0..k]*count[k+1...n]) 0 <= k < n-1

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.cache = {}
        return self.dfs(n)

    def dfs(self, n):
        if n in self.cache:
            return self.cache[n]
        if n == 1 or n == 0:
            return 1
        self.cache[n] = 0
        for i in range(n):
            self.cache[n] += self.dfs(i) * self.dfs(n - i - 1)
        return self.cache[n]


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 输出所有的可能性
# 每个数字都可以轮有做一次root, 然后左侧就 m 到 i-1的所有种可能
# 右侧就是 i+1 到n 的所有可能, 然后组合这些可能
class Solution2(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        self.cache = {}
        return self.dfs(1, n)

    def dfs(self, m, n):
        if (m,n) in self.cache:
            return self.cache[(m,n)]

        ret = []
        if m > n:
            return [None]
        for i in range(m, n + 1):
            left = self.dfs(m, i - 1)
            right = self.dfs(i + 1, n)
            for l in left:
                for r in right:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    ret.append(node)
        self.cache[(m, n)] = ret
        return self.cache[(m,n)]

if __name__ == '__main__':
    s = Solution2()
    s.generateTrees(3)
