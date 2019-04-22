class Solution:
    def compress(self, chars: List[str]) -> int:
        cur,count = 0,1
        while cur+1<len(chars):
            if chars[cur] == chars[cur+1]:
                chars.pop(cur+1)
                count += 1
            else:
                if count > 1:
                    tmp = list(str(count))
                    for i in range(len(tmp)):
                        chars.insert(cur + 1 + i, tmp[i])
                    # ['a', 'b', '1','2']
                    # chars.insert(cur+1, str(count))
                    cur += len(tmp) + 1
                    count = 1
                else:
                    cur += 1
        if count > 1:
            chars.extend(list(str(count)))
        # print(chars)
        return len(chars)
        
        
"""
"""
注意是o(1)
"""
这个是我写的代码 不过开辟了额外的空间 所以测试通不过 但是本地可以通过测试数据

class Solution:
    def compress(self, chars):
        """
        :type chars:List[str]
        :rtyp: int
        """
        i = 0

        while i < len(chars):
            temp = chars[i]
            num = chars.count(temp)
            num2 = num

            if num == 1:
                i = i + 1
                continue

            while temp in chars:
                chars.remove(temp)

            num = str(num)
            num = list(num)
            temp = list(temp) + num

            chars = chars[0:i] + temp + chars[i:]
            i = i + num2 + 1

        # print(chars)
        return len(chars)


def main():
    # result = Solution().compress(["a", "a", "b", "b", "c", "c", "c"])
    result = Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
    # result = Solution().compress(["a"])
    print(result)
    return result


if __name__ == "__main__":
    main()

 """
