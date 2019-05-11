# """
# 行： row = len(matrix)
# 列： col = len(matrix[0])
# i = row - 1
# j = 0
#
# 首先从左下角 matrix[i][j] 开始
# 只要 i< row and j < col -> i+=1 j+= 1
#
# """
#
#
# class Solution(object):
#     def isToeplitzMatrix(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: bool
#         """
#         row = len(matrix)
#         col = len(matrix[0])
#         i = row - 1
#         j = 0
#
#         while i in range(0, row) and j in range(0, col):
#
"""
除了首尾的两个对角
从最后一行开始除第一个元素 [5,1,2] == [5,1,2] 上一行出最后一个
[1,2,3] == [1,2,3]
"""
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if len(matrix) == 1:
            return True
        row = len(matrix)
        col = len(matrix[0])
        i = row - 1

        while i > 0:
            if matrix[i][1:col] != matrix[i-1][:col-1]:
                return False
            i -= 1

        return True


def main():
    # result = Solution().isToeplitzMatrix(matrix = [
    #                                       [1,2,3,4],
    #                                       [5,1,2,3],
    #                                       [9,5,1,2]
    #                                     ])
    result = Solution().isToeplitzMatrix(matrix = [[1,2],[2,2]])
    print(result)
    return result


if __name__ == '__main__':
    main()
