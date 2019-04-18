"""
while val in nums  -> nums.remove(val)
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)

        return len(nums)

def main():
    # 自定义测试用例
    result = Solution().removeElement([0,1,2,2,3,0,4,2],2)
    print(result)


if __name__ == '__main__':
    main()
