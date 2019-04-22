"""
要用到str->list函数了
不过前面要对的输入的数据进行判断是否合法
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == "":
            return 0
        s = s.strip(" ")
        s = s.split(" ")
        return len(s[-1])

def main():
    result = Solution().lengthOfLastWord("hello world ")
    print(result)
    return result

if __name__ == '__main__':
    main()
