"""
正整数

首先直接将这个数的二进制保存
然后将1变0 0变1  转十进制
"""


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = bin(num)
        num = num.replace("0b", "")

        num = num.replace('1','2')
        num = num.replace('0','1')
        num = num.replace('2','0')

        return int(num,2)

def main():
    # result = Solution().findComplement(5)
    result = Solution().findComplement(1)
    print(result)
    return result


if __name__ == '__main__':
    main()
