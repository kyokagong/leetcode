class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = nums1 + nums2
        nums3 = quick_sort(nums3)
        print(nums3)
        median = int(len(nums3) / 2)
        if len(nums3) % 2 == 0:
            return (nums3[median - 1] + nums3[median]) * 1. / 2
        else:
            return nums3[median]


def merge_sort(lst):
    result = []
    if len(lst) <= 1:
        return lst
    mid = int(len(lst) / 2)
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            result.append(right[0])
            right.pop(0)
        else:
            result.append(left[0])
            left.pop(0)
    result += left
    result += right
    return result


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
        if lst[i] <= pivot:
            left.append(lst[i])
        else:
            right.append(lst[i])
    result += quick_sort(left)
    result.append(pivot)
    result += quick_sort(right)
    return result

