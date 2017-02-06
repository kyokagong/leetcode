class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        nums.sort()
        print(nums)
        longestSeq = 1
        tmpLong = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                tmpLong += 1
            elif nums[i] - nums[i - 1] > 1:
                longestSeq = max(longestSeq, tmpLong)
                tmpLong = 1
                if longestSeq > (len(nums) / 2):
                    return longestSeq
        longestSeq = max(longestSeq, tmpLong)
        return longestSeq

if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]))