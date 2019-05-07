class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # return s[::-1]

        for i in range(int(len(s)/2)):
            s[i],s[len(s)-i-1] = s[len(s)-i-1],s[i]

def main():
    result = Solution().reverseString(["h", "e", "l", "l", "o"])
    print(result)
    return result


if __name__ == '__main__':
    main()
