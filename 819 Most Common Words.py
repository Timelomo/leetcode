'''
1. 处理paragraph 首先将大写全部转换为小写 然后将 各种标点符号全部替换
2.利用str->list函数将其转换为列表
3. 直接判断

注：python str方法
>>> dir("str")
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__',
 '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', 
 '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
 '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 
 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 
 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind',
 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
 
>>> dir([])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', 
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__',
 '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', 
 '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
 '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__',
 '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 
 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
 
 
 str->list 
>>> str1 = '1234'
>>> list1 = list(str1)
>>> list1
['1', '2', '3', '4']
>>> str2 = '123 456 ttt'
>>> list2 = str2.split()
>>> list3 = str2.split(" ")
>>> list2
['123', '456', 'ttt']
>>> list3
['123', '456', 'ttt']
>>>
>>> str3 = 'www.google.com'
>>> list4 = str3.split('.')
>>> list4
['www', 'google', 'com']

list->str
>>> list1
['www', 'google', 'com']
>>> str1 = "".join(list1)
>>> str1
'wwwgooglecom'
>>> str2 = ".".join(list1)
>>> str2
'www.google.com'
>>> str3 = " ".join(list1)
>>> str3
'www google com'
'''


# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        sym = ['!', '?', ',', ';', '.','\'']
        paragraph = paragraph.lower()
        for i in sym:
            paragraph = paragraph.replace(i, ' ')  # 将这些符号全部去除

        # 直接将banned的删除吧 懒得后面判断 in
        # for i in banned:
        #     paragraph = paragraph.replace(i, '')
        # "abc abc? abcd the jeff!",["abc","abcd","jeff"] 上面的不行 忽略了这样的情况

        # str -> list
        paragraph = paragraph.split()

        max = 0
        words = ''
        for i in paragraph:
            if max < paragraph.count(i) and i not in banned:  # 这个地方需要优化
                max = paragraph.count(i)
                words = i

        return words


def main():
    # result = Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
    # result = Solution().mostCommonWord("a, a, a, a, b,b,b,c, c",["a"])
    # result = Solution().mostCommonWord("abc abc? abcd the jeff!",["abc","abcd","jeff"])
    result = Solution().mostCommonWord("j. t? T. z! R, v, F' x! L; l! W. M; S. y? r! n;"
                                       " O. q; I? h; w. t; y; X? y, p. k! k, h, J, r? w! U! V; j' u; R! z. s. "
                                       "T' k. P? M' I' j! y. P, T! e; X. w? M! Y, X; G; d, X? S' F, K? V, r' v, "
                                       "v, D, w, K! S? Q! N. n. V. v. t? t' x! u. j; m; n! F, V' Y! h; c! V, v, X' "
                                       "X' t? n; N' r; x. W' P? W; p' q, S' X, J; R. x; z; z! G, U; m. P; o. P! Y; I,"
                                       " I' l' J? h; Q; s? U, q, x. J, T! o. z, N, L; u, w! u, S. Y! V; S? y' E! O; p' X,"
                                       " w. p' M, h! R; t? K? Y' z? T? w; u. q' R, q, T. R? I. R! t, X, s? u; z. u, Y, n' U; "
                                       "m; p? g' P? y' v, o? K? R. Q? I! c, X, x. r' u! m' y. t. W; x! K? B. v; m, k; k' x; "
                                       "Z! U! p. U? Q, t, u' E' n? S' w. y; W, x? r. p! Y? q, Y. t, Z' V, S. q; W. Z, z? x! "
                                       "k, I. n; x? z; V? s! g, U; E' m! Z? y' x? V! t, F. Z? Y' S! z, Y' T? x? v? o! l; d; "
                                       "G' L. L, Z? q. w' r? U! E, H. C, Q! O? w! s? w' D. R, Y? u. w, N. Z? h. M? o, B, g, Z! "
                                       "t! l, W? z, o? z, q! O? u, N; o' o? V; S! z; q! q. o, t! q! w! Z? Z? w, F? O' N' U' p? r' "
                                       "J' L; S. M; g' V. i, P, v, v, f; W? L, y! i' z; L? w. v, s! P?",
                                       ["m","q","e","l","c","i","z","j","g","t","w","v","h","p","d","b","a","r","x","n"])
    print(result)
    return result


if __name__ == '__main__':
    main()


'''
也可以使用正则表达式的方法 更加的方便
import re

# 没让不用正则啊
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s = paragraph.lower()  # 字符串转换成小写
        a = re.findall(r"[a-z]+",s)  # 正则匹配单词
        set_ = set(a)  # set去重
        dict_ = {}
        for i in set_:  # 遍历去重的结果,并判断是否在禁用的单词列表中
            if i not in banned:
                b = a.count(i)
                dict_[i] = b

        s1 = max(dict_, key=dict_.get)  # 字典求最大键值的方法
        return s1
'''
