#-*-coding:utf-8-*-#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 每次检验本接节点是否值大于最小,大于最大值,
# 节点左侧的所有值一定是小于本节点值,即本节点值为左节点的最大值
# 节点右侧的所有值一定是大于本节点值,即本节点值为右节点的最小值
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    def isValidBST(self, root):
        return self.isValidBSTImpl(root, -2**31, 2**31 - 1)

    def isValidBSTImpl(self, root, min, max):
        if root == None:
            return True
        return root.val > min and root.val < max and\
               self.isValidBSTImpl(root.left, min, root.val) and \
               self.isValidBSTImpl(root.right, root.val, max)

if __name__ == '__main__':
    node = TreeNode(10)
    node.left = TreeNode(5)
    node.right = TreeNode(15)
    node.right.left = TreeNode(6)
    node.right.right = TreeNode(20)
    s = Solution()
    print(s.isValidBST(node))