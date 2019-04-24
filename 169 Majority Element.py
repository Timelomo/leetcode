"""
由于这里的众数是超过 n/2 所以直接sort 然后取中间的那个就是众数

不需要先sort() 然后remove 再去count 找找最大值
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) // 2]


def main():
    result = Solution().majorityElement([2, 2, 1, 1, 1, 2, 2])
    print(result)
    return result


if __name__ == '__main__':
    main()
