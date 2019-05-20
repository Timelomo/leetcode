"""
我的想法
首先全部转换成 小写
然后遍历 处理 一次处理一个 很复杂


but
下面代码 niu X

"""


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = ['']
        for c in S:
            res = [i + c for i in res] + [i + c.swapcase() for i in res if c.isalpha()]
        return res


def main():
    result = Solution().letterCasePermutation(S="a1b2")
    print(result)
    return result


if __name__ == '__main__':
    main()
