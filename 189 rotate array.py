class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return
        real_k = k % len(nums)
        nums[0:len(nums)-real_k],nums[len(nums)-real_k:] = nums[len(nums)-real_k:],nums[0:len(nums)-real_k]
## 直接前后交换

## 更好的方法
class Solution(object):
	def rotate(self,nums,k):
		for i in range(k):
			nums.insert(0,nums.pop(-1))
