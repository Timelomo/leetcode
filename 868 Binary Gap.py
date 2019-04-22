"""
通过index方法每次去找相邻最近的那个 然后往后递推
"""
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = bin(N).replace('0b', '')

        if s.count('1') < 2:
            return 0

        max_length = 0
        distance = 0
        start = 0
        end = 0
        start = s.index('1', start) # 首先找到第一起点位置

        while start < len(s):
            end = s.index('1', start + 1)

            distance = end - start

            if distance > max_length:
                max_length = distance

            start = end

            if s.count('1', start+1) == 0:
                break

        return max_length


def main():
    # result = Solution().binaryGap(22)
    result = Solution().binaryGap(10**9)
    print(result)
    return result


if __name__ == "__main__":
    main()
