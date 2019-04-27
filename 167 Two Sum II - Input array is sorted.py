"""
法1 首先定index1 然后用target - index1[] = index2 查询index2是否在里面
并且不重复


法2 使用哈希表
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # answer = []
        #
        # for i in range(len(numbers)):
        #     number1 = numbers[i]
        #     number2 = target - number1
        #     if number2 in numbers[i+1:]:
        #         answer.append(i+1)
        #         answer.append(numbers.index(number2,i)+1)
        #         break
        #
        # return answer
        d = {}
        for i, n in enumerate(numbers):
            another_num = target - n
            if another_num in d:
                return [d[another_num] + 1, i + 1]
            d[n] = i

def main():
    # result = Solution().twoSum([2, 7, 11, 15], 9)
    result = Solution().twoSum([0,0,3,4],0)
    print(result)
    return result


if __name__ == "__main__":
    main()
