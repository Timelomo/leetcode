'''
1. 转变成str
            2. 对负号的处理xxx 不需要处理
3. 用一个变量s 保存 翻转后的 str
4. 若 s == str 则return true
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s1 = str(x)
        s2 = s1[::-1]

        if s1 == s2:
            return True
        else:
            return False
        # 写个 true false 什么意思...... 我还以为返回 字符串 true或者 false

def main():
    result = Solution().isPalindrome(121)
    print(result)


if __name__ == '__main__':
    main()
