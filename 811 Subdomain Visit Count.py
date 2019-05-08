"""
利用一字典来存储
遍历这个列表 然后 对每个字符串

首先 分割出次数 然后 每次按照 . 的位置进行分割
"""


class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        # d = {}
        # for i in cpdomains:
        #     l = i.split(" ")
        #     num = int(l[0])
        #
        #     while '.' in l[1]:
        #         if l[1] in d.keys():
        #             d[l[1]] += num
        #         d[l[1]] = num
        #
        #         l[1] = l[l[1].index('.')+1:]
        #
        #     if l[1]: # 忘记判断里面最后一个没有 '.'的情况了 参考了人家的代码 基本思想是一样的
        #         if l[1] in d.keys():
        #             d[l[1]] += num
        #         d[l[1]] = num
        #
        # return d
        d = {}
        for i in cpdomains:
            c, j = i.split()
            while True:
                if j in d:
                    d[j] += int(c)
                else:
                    d[j] = int(c)

                f = j.find('.')
                if f == -1:
                    break
                else:
                    j = j[f + 1:]

        res = list(d.keys())
        answer = []
        for i in res:
            t = str(d[i]) + " " + str(i)
            answer.append(t)
        return answer


def main():
    result = Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
    print(result)
    return result


if __name__ == "__main__":
    main()
