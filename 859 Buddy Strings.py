"""
首先判断两个字符串中的长度 以及元素是否相同
sort 然后进行比较 如果不相同直接 false

设置两个flag 循环遍历AB 原始字符串 如果有两个不同的返回true
其他情况 False

"""


class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        a = list(A)
        b = list(B)
        a.sort()
        b.sort()

        if a != b:
            return False

        num = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                num += 1

        if num == 2:
            return True
        elif num == 0:  # 这个时候AB两个内容一致 就要去判断A中是否有两个元素是相同的即可
            if len(set(A)) == len(A):
                return False
            else:
                return True
        else:
            return False


def main():
    # result = Solution().buddyStrings("ab", "ba")
    # result = Solution().buddyStrings(A = "aaaaaaabc", B = "aaaaaaacb")
    result = Solution().buddyStrings(A="ab", B="ab")
    # result = Solution().buddyStrings(A="aa", B="aa")
    print(result)
    return result


if __name__ == '__main__':
    main()
