"""
库函数无敌

1. 看是否在里面 如果在 就直接 index
2. 不在 首先直接插入 然后 sort 再 index
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)

def main():
    # result = Solution().searchInsert([1,3,5,6],5)
    # result = Solution().searchInsert([1,3,5,6],2)
    # result = Solution().searchInsert([1,3,5,6],7)
    result = Solution().searchInsert([1,3,5,6],0)
    print(result)
    return result

if __name__ == '__main__':
    main()
