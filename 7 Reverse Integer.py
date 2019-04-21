'''
>>> 2**31
2147483648
>>> 2**31-1
2147483647

1. 判断正负号
2. 直接翻转
3. 去除左边的0
4. 比较是否溢出
5. 输出

假设我们的环境只能存储得下 32 位的有符号整数，
则其数值范围为 [−231,  231 − 1]。请根据这个假设，
如果反转后整数溢出那么就返回 0。
所以这样的话 直接 int() 就不行 用字符串进行比较
'''


class Solution:
    def reverse(self, x: int) -> int:
        maxBorder = "2147483647"
        minBorder = "2147483648"

        # 哈哈哈哈哈哈哈哈哈哈用了 lstrip('0')忘记了 只有0的这种情况
        if x == 0:
            return 0

        isNegativeNumber = False  # 代表是负数
        if x < 0:
            isNegativeNumber = True

        s = str(x)

        if isNegativeNumber:
            s = s[:0:-1]  # 翻转除去了第一位的负号
        else:
            s = s[::-1]

        s = s.lstrip('0')  # 去除左边0

        try:
            if isNegativeNumber:  # 负数比较是否溢出
                if len(s) >= len(minBorder) and s > minBorder:
                    return 0
                else:
                    s = '-' + s
                    return int(s)
            else:
                if len(s) >= len(maxBorder) and s > maxBorder:
                    return 0
                else:
                    s = int(s)
                    return s

        except Exception as e:
            print(e)

def main():
    test = Solution().reverse(0)
    print(test)


if __name__ == '__main__':
    main()
