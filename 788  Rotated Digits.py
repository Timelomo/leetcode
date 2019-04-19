class Solution:
    def rotatedDigits(self, N: int) -> int:
        l = ['2', '5', '6', '9','0','1','8']
        d = {
            '0': '0',
            '1': '1',
            '2': '5',
            '3': 's',
            '4': 's',
            '5': '2',
            '6': '9',
            '7': 's',
            '8': '8',
            '9': '6'
        }
        count = 0

        for i in range(1, N + 1):
            s = str(i)

            rs = ''

            flag = True  # 首先认为是好数

            for j in s:
                if j not in l:
                    flag = False
                    break

            if flag:
                for i in range(len(s)):
                    rs += d[s[i]]

                if rs == s:  # 和原来的数x要不同
                    flag = False

            if flag:
                count += 1

        return count

def main():
    result = Solution().rotatedDigits(857)
    print(result)


if __name__ == '__main__':
    main()
