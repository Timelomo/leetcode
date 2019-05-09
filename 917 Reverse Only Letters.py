"""
str-> list
首尾指针 进行同时遍历并判断
i<=j 停止
list->str
"""


class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        l = list(S)
        i = 0
        j = len(l) - 1

        while i <= j:
            if not l[i].isalpha():
                i += 1
                continue
            if not l[j].isalpha():
                j -= 1
                continue

            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1

        return "".join(l)


def main():
    # result = Solution().reverseOnlyLetters("ab-cd")
    # result = Solution().reverseOnlyLetters("a-bC-dEf-ghIj")
    result = Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!")
    print(result)
    return result


if __name__ == "__main__":
    main()
