#-*-coding:utf-8-*-#
# 先排序,然后用两端逼近法,注意重复数字
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []

        nums.sort()
        i = 0
        while i < len(nums)-2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    ret.append([nums[i], nums[j], nums[k]])

                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1

            while i < len(nums) - 2 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-2,0,1,1,2]))