"""
判断只有一个的情况

选择一个最大的 然后就遍历数组进行比较
"""


class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Max = max(nums)
        loc = nums.index(Max)

        if len(nums) == 1:
            return loc

        nums.remove(Max)

        for i in range(len(nums)):
            if 2 * nums[i] > Max:
                return -1

        return loc


def main():
    # result = Solution().dominantIndex([3, 6, 1, 0])
    result = Solution().dominantIndex(nums=[1, 2, 3, 4])
    print(result)
    return result


if __name__ == "__main__":
    main()
