"""
找到最大的那个值 然后 看左边和右边 首先左右要非空 其次都是依次递减的


emmm 不过题目的意思是 答案一定存在 那么就 直接这样就行了

"""


class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        Max = max(A)
        return A.index(Max)


def main():
    result = Solution().peakIndexInMountainArray([0, 1, 0])
    print(result)
    return result


if __name__ == '__main__':
    main()
