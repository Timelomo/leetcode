"""
首先先找出所有c的位置 然后进行比较选择最小的
- 在同一个位置
- 位置差值最小的
"""

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        # 跟我的思路一样 不过我没处理好 后面的部分
        import re
        loc = [m.start() for m in re.finditer(C, S)]  # 寻找所在位置
        distance = []
        for i in range(len(S)):
            distance.append(min([abs(x - i) for x in loc]))

        return distance


def main():
    result = Solution().shortestToChar(S="loveleetcode", C='e')
    print(result)
    return result


if __name__ == "__main__":
    main()
