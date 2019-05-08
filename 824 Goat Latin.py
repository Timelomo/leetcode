class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        s = S.split(" ")
        l = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(len(s)):
            if s[i][0] in l:
                s[i] = s[i] + "ma" + (i + 1) * 'a'
            else:
                s[i] = s[i] + s[i][0]
                s[i] = s[i][1:]
                s[i] = s[i] + "ma" + (i + 1) * 'a'
        return " ".join(s)


def main():
    # result = Solution().toGoatLatin("I speak Goat Latin")
    result = Solution().toGoatLatin("The quick brown fox jumped over the lazy dog")
    print(result)
    return result


if __name__ == "__main__":
    main()
