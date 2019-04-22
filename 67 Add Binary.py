"""
思路1 转换字符串 一个个的加  可以实现

思路2 直接转为十进制 然后相加 再转二进制
>>> a= "11"
>>> b="1"
>>> int(a)
11
>>> int(a,2)
3
>>> int(b,2)
1
>>> c = 4
>>> bin(c)
'0b100'
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_a = int(a,2)
        num_b = int(b,2)

        sum = num_a+num_b

        return bin(sum).replace('0b',"")

def main():
    result = Solution().addBinary(a = "1010", b = "1011")
    print(result)
    return result


if __name__ == '__main__':
    main()
