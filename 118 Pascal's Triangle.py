class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        L = [[1], [1, 1]]

        for row in range(2, numRows):
            l = []
            l.append(L[row - 1][0])  # 新的一行第一个等于上一行的第一个 实际上就是1
            for i in range(1, len(L[row - 1])):
                l.append(L[row - 1][i] + L[row - 1][i - 1])
            l.append(L[row - 1][-1]) # 新的一行最后一个等于上一行的最后一个 实际上就是1
            L.append(l)

        return L


def main():
    result = Solution().generate(5)
    print(result)
    return result


if __name__ == '__main__':
    main()
