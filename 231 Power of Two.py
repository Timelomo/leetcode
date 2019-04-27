"""

如果输入的是奇数 并且不是1 直接 False
如果输入的是偶数 
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 2 != 0:
            if n == 1:
                return True
            return False
        i = 1
        t = 2 ** i
        while (t < n):
            i += 1
            t = 2 ** i

        if t == n:
            return True

        return False  # 这里是t > n


def main():
    # result = Solution().isPowerOfTwo(128)
    result = Solution().isPowerOfTwo(218)
    print(result)
    return result


if __name__ == "__main__":
    main()
