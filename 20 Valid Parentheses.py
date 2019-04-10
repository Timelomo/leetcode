"""
使用栈
1. len(str)  然后开始循环整个字符串
2. [ ( { 入栈 ] ) } 出栈 出栈时比较是否对应 否则返回false
3. 循环完整个字符串之后 栈必须为空 否则false

空字符串可被认为是有效字符串，所以第一步判空
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        d = {'}': '{', ']': '[', ')': '('}
        l = []
        length = len(s)
        i = 0
        j = 0 # 栈指针

        while (i < length):
            if s[i] in ['{', '[', '(']: # 入栈
                l.append(s[i])
                j += 1
            elif s[i] in ['}', ']', ')']: # 出栈
                if len(l) and l[j-1] == d.get(s[i]):
                    l.pop()
                    j -= 1
                else:
                    return False

            else:
                return False

            i += 1

        if len(l)==0: # 最后不为空 则出错
            return True
        else:
            return False

def main():
    result = Solution().isValid("{[]}")
    print(result)


if __name__ == '__main__':
    main()


"""
附上大佬的代码
class Solution:
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''
"""
