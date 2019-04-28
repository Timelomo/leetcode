"""
1. 首先将数组sort
2. 遍历数组 如果count(i) == 2 那么就i+=2
3. 否则直接输出该数


采用异或的方法
交换律：a ^ b ^ c <=> a ^ c ^ b
任何数于0异或为任何数 0 ^ n => n
相同的数异或为0: n ^ n => 0
"""

''' 算法超时了 最后一个测试数据通不过
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        while (i < len(nums)):
            if nums.count(nums[i]) == 2:
                i += 2
            else:
                return nums[i]
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for num in nums:
            a = a^num
        return a



def main():
    # result = Solution().singleNumber([2, 2, 1])
    result = Solution().singleNumber([4,1,2,1,2])
    print(result)
    return result


if __name__ == '__main__':
    main()
