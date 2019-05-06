"""
首先分割为list

count(xx) = 1 and not in Another -> not in answer -> answer.append(xx)
"""

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a = A.split(" ")
        b = B.split(" ")
        l = []

        for i in a:
            if a.count(i) == 1 and i not in b:
                l.append(i)

        for i in b:
            if b.count(i) == 1 and i not in a:
                l.append(i)

        return l

def main():
    # result = Solution().uncommonFromSentences(A = "this apple is sweet", B = "this apple is sour")
    result = Solution().uncommonFromSentences(A = "apple apple", B = "banana")
    print(result)
    return result


if __name__ == '__main__':
    main()


"""
方法2
s = A + " " + B 
s = s.split(" ")
s_set = set(s)
l = []
for i in s_set:
    if s.count(i) == 1:
        l.append(i)
return l
"""
