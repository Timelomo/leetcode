"""
判断LR
UD 这两个的数量分别是否相等即可
"""


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if moves.count('D') == moves.count('U') and moves.count('L') == moves.count('R'):
            return True
        else:
            return False


def main():
    result = Solution().judgeCircle("UD")
    print(result)
    return result


if __name__ == "__main__":
    main()
