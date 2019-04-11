"""
1. 判断非空
2. 两个指针
"""

class Solution:
    def removeDuplicates(self, nums):
        if nums:
            j = 0

            for i in range(len(nums)-1):
                if nums[i] != nums[i+1]:
                    nums[j] = nums[i]
                    j += 1

            nums[j] = nums[len(nums)-1]

            return j+1
        else:
            return 0

def main():
    # 自定义测试用例
    rList = Solution().removeDuplicates([0,1,1,2,2,3,3])
    print(rList)


if __name__ == '__main__':
    main()
