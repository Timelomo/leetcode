"""

直接遍历 时间复杂度 O(n) 在判断下一个同时 先判断一一下这个字符的长度是否 >=3
记录只要 相同 就继续遍历下去 然后记录 end 和 start 直到最后
"""


class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        if len(S) < 3:
            return []

        ans = []
        length = len(S)
        i = 0
        while i <= length - 3:
            if S[i:].count(S[i]) < 3:
                i += 1
                continue

            if S[i + 1] == S[i] and S[i + 2] == S[i]:
                start = end = i
                while i < length - 1 and S[i + 1] == S[i]:  # 注意这里不要越界了
                    end += 1
                    i += 1
                ans.append([start, end])

            i += 1

        return ans


def main():
    # result = Solution().largeGroupPositions("abbxxxxzzy")
    # result = Solution().largeGroupPositions("abcdddeeeeaabbbcd")
    # result = Solution().largeGroupPositions("abc")
    # result = Solution().largeGroupPositions("aaaa")
    result = Solution().largeGroupPositions("aaa")
    print(result)
    return result


if __name__ == '__main__':
    main()
