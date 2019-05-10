"""
0^1 = 1
1^1 = 0
"""


class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for l in range(len(A)):
            for i in range(len(A[l])):
                A[l][i] ^= 1

        for l in range(len(A)):
            # print(A[l])
            A[l].reverse()

        return A


def main():
    result = Solution().flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]])
    print(result)
    return result


if __name__ == '__main__':
    main()
