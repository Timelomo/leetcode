'''
考察的是kmp算法
不过 调用库函数的感觉真的爽歪歪
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

def main():
    # 自定义测试用例
    result = Solution().strStr("hello","o")
    print(result)


if __name__ == '__main__':
    main()
