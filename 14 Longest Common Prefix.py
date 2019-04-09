class Solution:
    # def longestCommonPrefix(self, strs: list[str]) -> str:
    def longestCommonPrefix(self, strs):
        len_strs = len(strs)
        if len_strs == 0:
            return ""
        elif len_strs == 1:
            return strs[0]
        cur = strs[0]
        for str in strs[1:len_strs]:
            min_len = min(len(cur), len(str))
            temp = ""
            for i in range(0, min_len):
                if str[i] == cur[i] :
                    temp = cur[0:i + 1]
                else:
                    break
            cur = temp
            if cur == "":
                break
        return cur
def main():
    result = Solution().longestCommonPrefix(["flower","flow","flight"])
    print(result)


if __name__ == '__main__':
    main()
