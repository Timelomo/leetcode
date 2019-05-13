"""
进行互换即可
但是用一下 numpy 直接进行 矩阵转置
"""


class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        import numpy
        a = numpy.transpose(A)
        a.tolist()
        return a
        # return [*zip(*A)]

def main():
    result = Solution().transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(result)
    return result


if __name__ == '__main__':
    main()
