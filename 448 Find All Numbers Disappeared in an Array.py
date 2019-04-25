"""
首先将数组转为set去除相同元素
然后转为list 升序排序
按照下标进行循环一遍 如果 下标+1 等于该数 就代表存在
否则的话insert  并保存
"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        l = []
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        nums.append(-1)

        for i in range(length):
            if i + 1 == nums[i]:
                nums[i] = -1
            else:
                nums.insert(i, i + 1)
                l.append(i+1)


        return l


def main():
    result = Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
    print(result)
    return result


if __name__ == '__main__':
    main()
