class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = bin(n)
        s = s.replace("0b","")
        num = s.count("1")
        return num

def main():
    result = Solution().hammingWeight(5)
    print(result)
    return result


if __name__ == '__main__':
    main()
