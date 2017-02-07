#-*-coding:utf-8-*-#
# 方法很简单， 就是制作循环的链表，然后第二次再找出断点，将其next=None
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None

        first_head = head
        length = 1

        while head.next is not None:
            length += 1
            head = head.next
        head.next = first_head

        m = k % length

        for i in range(length - m):
            head = head.next

        n_head = head.next
        head.next = None
        return n_head


if __name__ == '__main__':
    s = Solution()
