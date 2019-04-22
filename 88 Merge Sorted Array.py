"""
直接字符串拼接 然后sort
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # nums1 = nums1[0:m] + nums2[0:n]
        nums1[m:len(nums1)] = nums2[0:n]
        nums1.sort()

        # return nums1


def main():
    result = Solution().merge(nums1 = [1,2,3,0,0,0], m = 3,nums2 = [2,5,6],n = 3)
    print(result)
    return result

if __name__ == '__main__':
    main()
