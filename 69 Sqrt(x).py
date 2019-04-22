"""
库函数调用一时爽 一直调 一直爽
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        import math
        return int(math.sqrt(x))



def main():
    result = Solution().mySqrt(100)
    print(result)
    return result

if __name__ == '__main__':
    main()
