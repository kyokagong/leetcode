#-*-coding:utf-8-*-#
"""
桶的方法 O(n)

思想是分成t+1个桶，对于一个数，将其分到第num / (t + 1) 个桶中，我们只需要查找相同的和相邻的桶的元素就可以判断有无重复。

比如t = 4，那么0~4为桶0，5~9为桶1，10~14为桶2  然后你懂的- –
"""
import collections
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        """ :type nums: List[int] :type k: int :type t: int :rtype: bool """
        if k < 1 or t < 0:
            return False
        dicts = collections.OrderedDict()

        for i in range(len(nums)):
            key = nums[i] / max(1, t)
            for m in (key - 1, key, key + 1):
                if m in dicts and abs(nums[i] - dicts[m]) <= t:
                    return True
            dicts[key] = nums[i]
            if i >= k:
                dicts.popitem(last=False)
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyAlmostDuplicate([1,3,1], 2, 1))
    print(s.containsNearbyAlmostDuplicate([1,2], 0, 1))
    print(s.containsNearbyAlmostDuplicate([7,2,8],2,1))