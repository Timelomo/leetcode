"""
思路 
利用set 将set之后的结果保存 
l = set(nums) 如果 len(l) = len(nums) 表示没有重复的
否则就是有重复的
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set(nums)
        if len(s) == len(nums):
            return False
        else:
            return True


def main():
    # result = Solution().containsDuplicate([1, 2, 3, 4])
    result = Solution().containsDuplicate([1, 2, 3, 4,3])
    print(result)
    return result


if __name__ == '__main__':
    main()
