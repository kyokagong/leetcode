#-*-coding:utf-8-*-#

# 就是链表数据结构题
# 一般做法是定义一个虚拟的头,这个头的next就是输入head, p = tmpHead.next
# 然后 p.next 和 p.next.next都不会空才做交换, p.next.next为空返回p.next

# 所以根据这个性质,我做了一个递归的方法,看上去更简洁

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        return self.dfs(head, head.next)

    def dfs(self, first, second):
        if second is None:
            return first
        first.next = second.next
        second.next = first
        if first.next is not None:
            first.next = self.dfs(first.next, first.next.next)
        return second