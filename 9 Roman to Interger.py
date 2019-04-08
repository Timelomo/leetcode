class Solution:
    def romanToInt(self, s: str) -> int:
        d1 = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        d2 = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        length = len(s)
        i = 0
        sum = 0

        while(i<length):
            if( d2.get(s[i:i+2]) ):
                sum = sum + d2.get(s[i:i+2])
                i = i+1
            else:
                sum = sum + d1.get(s[i])

            i+= 1
        return sum

def main():
    result = Solution().romanToInt("MCMXCIV")
    print(result)


if __name__ == '__main__':
    main()
