"""
把一个作为定 然后判断另外一个四个点是否在这个区域内部

或则判断 重叠部分的面积是否大于0
"""

# error
# class Solution(object):
#     def isRectangleOverlap(self, rec1, rec2):
#         """
#         :type rec1: List[int]
#         :type rec2: List[int]
#         :rtype: bool
#         """
#         x_range = [min(rec1[0], rec1[2]), max(rec1[0], rec1[2])]
#         y_range = [min(rec1[1], rec1[3]), max(rec1[1], rec1[3])]
#
#         if x_range[0] <= rec2[0] <= x_range[1] and y_range[0] <= rec2[1] <= y_range[1]:
#             return True
#         if x_range[0] <= rec2[2] <= x_range[1] and y_range[0] <= rec2[3] <= y_range[1]:
#             return True
#         # if y_range[0] < rec2[1] < y_range[1]:
#         #     return True
#         # if y_range[0] < rec2[3] < y_range[1]:
#         #     return True
#
#         return False

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        [A, B, C, D], [E, F, G, H] = rec1, rec2
        x, y = (min(C, G) - max(A, E)), (min(D, H) - max(B, F))
        return x > 0 and y > 0


def main():
    # result = Solution().isRectangleOverlap(rec1=[0, 0, 2, 2], rec2=[1, 1, 3, 3])
    # result = Solution().isRectangleOverlap(rec1=[0, 0, 1, 1], rec2=[1, 0, 2, 1])
    # result = Solution().isRectangleOverlap([5, 15, 8, 18], [0, 3, 7, 9])
    result = Solution().isRectangleOverlap([7, 8, 13, 15], [10, 8, 12, 20])
    print(result)
    return result


if __name__ == '__main__':
    main()
