"""
首先利用三个 列表保存 这三行
然后 循环遍历列表中的字符串

"""


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        l = []
        answer = []
        l1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        l2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        l3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

        for i in words:
            p = i.lower()
            flag = False
            if p[0] in l1:
                l = l1
            elif p[0] in l2:
                l = l2
            elif p[0] in l3:
                l = l3

            for j in p:
                if j not in l:
                    flag = True
                    break

            if not flag:
                answer.append(i)

        return answer


def main():
    result = Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])
    print(result)
    return result


if __name__ == '__main__':
    main()
