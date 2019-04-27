"""
方法一： 
转为二进制之后 在左边填充0字符 或者 直接从右边开始比较
然后多的地方就直接和0比较 循环字符串进行每个字符的比较

方法二：
通过异或算法 直接能够求出结果
"""

'''
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = bin(x).replace("0b", "")
        y = bin(y).replace("0b", "")
        count = 0
        # 事先将两个字符串进行前面补0 
        x = x.rjust(32, '0')
        y = y.rjust(32, '0')

        for i in range(0, 32):
            if x[i] != y[i]:
                count += 1

        return count
'''
#  方法二
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        return bin(x ^ y).count('1')


def main():
    result = Solution().hammingDistance(1, 2)
    print(result)
    return result


if __name__ == '__main__':
    main()
