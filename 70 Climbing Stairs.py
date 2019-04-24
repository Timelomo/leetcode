"""
一开始准备用打表法
结果在纸上面一推才知道这个是一个斐波那契
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        l = [0,1,2]

        for i in range(3,n+1):
            l.append(l[i-1]+l[i-2])

        return l[-1]



def main():
    result = Solution().climbStairs(6)
    print(result)
    return result


if __name__ == '__main__':
    main()
