"""
用最接近的那个去消除
考虑类似于c++ 中的lower_bound() 的方法

倒着遍历s表 如果g中有相同的元素 直接消除
如果没有的话
"""


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        sum = 0
        g.sort()
        s.sort()

        m = len(g)
        n = len(s)

        j = 0
        i = 0

        while i < m and j < n:
            if g[i] <= s[j]:
                j += 1
                i += 1
                sum += 1
            else:
                j += 1
        return sum


def main():
    # result = Solution().findContentChildren([1, 2, 3], [1, 1])
    result = Solution().findContentChildren([1, 2], [1, 2, 3])
    print(result)
    return result


if __name__ == '__main__':
    main()
