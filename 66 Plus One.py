"""
先List-> str
str->int
int + 1
int -> str
str-> list
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = list(map(str, digits))
        s = "".join(digits) # 此处忽略了digits是一个数字列表通过上面进行修改
        num = int(s)
        num = num+1
        s = str(num)
        digits = list(s)

        digits = list(map(int, digits)) # 将['x','y']改为 [x,y]
        return digits


def main():
    result = Solution().plusOne([1,2,3])
    print(result)
    return result


if __name__ == '__main__':
    main()
