#-*-coding:utf-8-*-#

# 排序题, 就是排序的比较方法不一样
# nums[i] + num[i+1] > nums[i+1] + num[i] 则不用交换位置,不然交换位置
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        ret = ''.join([str(item) for item in quick_sort(nums)])

        # below is preventing '00' or '000' etc
        ans = ''.join(ret).lstrip('0')
        return ans or '0'


import random
def quick_sort(lst):
    result = []
    if len(lst) <= 1:
        return lst
    ran_ind = random.randint(0, len(lst) - 1)
    pivot = lst[ran_ind]
    lst.pop(ran_ind)
    left = []
    right = []
    for i in range(len(lst)):
        if _isLarger(lst[i], pivot):
            left.append(lst[i])
        else:
            right.append(lst[i])
    result += quick_sort(left)
    result.append(pivot)
    result += quick_sort(right)
    return result

# this means that ab > ba, so we need to put b afront of a.
# this is a descending array
def _isLarger(a, b):
    if str(a) + str(b) > str(b) + str(a):
        return True
    else:
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.largestNumber([20,1]))
