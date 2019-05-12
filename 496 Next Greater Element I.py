"""
常规方法

"""


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums1:
            loc = nums2.index(i)
            if loc == len(nums2) - 1:
                res.append(-1)
                continue

            temp = nums2[loc + 1:]

            if temp and max(temp) < i:
                res.append(-1)
            else:
                for j in temp:
                    if j >= i:
                        res.append(j)
                        break
        return res


def main():
    # result = Solution().nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2])
    result = Solution().nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4])
    print(result)
    return result


if __name__ == '__main__':
    main()
