"""
>>> for i in range(10,0,-1):
	print(i)


10
9
8
7
6
5
4
3
2
1

计算 5 的个数即可

"""


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 超时算法
        # count = 0
        # a = 1
        # for i in range(1, n + 1):
        #     a = a * i
        #
        # a = str(a)
        # a = a[::-1]
        # for i in range(len(a)):
        #     if a[i] == '0':
        #         count += 1
        #     else:
        #         break
        #
        # return count

        ################
        # Line 24: MemoryError
        # 最后执行的输入：
        # 1808548329

        # count = 0
        # for i in range(n, 0, -1):
        #     t = i
        #     if t % 5 == 0:
        #         while (t >= 5 and t % 5 == 0):
        #             count += 1
        #             t = t / 5
        #
        # return count

        i = 0
        while(n>=5):
            n = int(n/5)
            i += n
        return i

def main():
    # result = Solution().trailingZeroes(5)
    # result = Solution().trailingZeroes(1808548329)
    result = Solution().trailingZeroes(25)
    print(result)
    return result


if __name__ == '__main__':
    main()
