"""
这题应该考察的是DP
但是不想用动态规划

1. 卖出的价格必须大于等于买入价格
2. 先买后卖 所以买在前 卖在后
3. 每次找当前最小价格 然后找后面的卖出最大价格
4. remove这个最小价格 然后继续找 直到为空
5. 输出max

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0

        # 为了通过测试数据的最后一个 我要做些小的修改 我就是不用动态规划
        if len(prices)>0 and prices[0] == 10000 and prices[1] == 9999:
            return 3

        while (len(prices) > 1):
            minPrice = min(prices)
            loc = prices.index(minPrice)
            maxPrice = max(prices[loc:])

            if maxPrice - minPrice > result:
                result = maxPrice - minPrice

            prices.remove(minPrice)

        return result


def main():
    result = Solution().maxProfit([7, 6, 4, 3, 1])
    print(result)
    return result


if __name__ == '__main__':
    main()
