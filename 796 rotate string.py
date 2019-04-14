"""
1. 判断字符串是否为空
两个都为空的 则返回true

有一个不为空 就返回false

2. 判断长度是否相等

3. 定 A 变换 B len(B)次 看是否和A相等 如果相同返回True 循环完了还是不相等就是Flase

"""


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if (len(A) != len(B)):
            return False
        if (A == "" and B == ""):
            return True
        elif A == "" or B == "":
            return False

        k = 0
        while(k<len(B)):
            s = B[len(B)-k-1:len(B)] + B[0:len(B)-k-1] # 注意下标
            if s == A:
                return True
            else:
                k += 1
        return False

def main():
    result = Solution().rotateString('abcde', 'abced')
    print(result)


if __name__ == '__main__':
    main()
