"""
0. 如果是空的字符串直接return True
1. 将所有大写全部改为小写
2. 删除除了是字母或者数字
3. 将新的字符串翻转比较是相同
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        s = s.lower()
        l = []
        for i in range(len(s)):
            if s[i].isalnum():
                l.append(s[i])

        l2 = l[::-1]

        if l2 == l:
            return True
        else:
            return False

def main():
    # result = Solution().isPalindrome("A man, a plan, a canal: Panama")
    result = Solution().isPalindrome("race a car")
    print(result)
    return result


if __name__ == '__main__':
    main()
