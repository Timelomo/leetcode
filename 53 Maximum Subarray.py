"""
考到算法了 要用动态规划的思想来解决
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        curMax = 0

        for i in nums:
            curMax = max(curMax,0) + i
            res = max(curMax,res)

        return res


def main():
    result = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(result)
    return result


if __name__ == '__main__':
    main()
