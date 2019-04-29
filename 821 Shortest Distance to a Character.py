"""
首先先找出所有c的位置 然后进行比较选择最小的
- 在同一个位置
- 位置差值最小的
"""
"""
class Solution(object):
    def shortestToChar(self, S, C):
        """
:type
S: str
:type
C: str
:rtype: List[int]
"""
loc_C = []
loc = []
for i in range(len(S)):
    if S[i] == C:
        loc_C.append(i)

for i in range(len(S)):
    if i in loc_C:
        loc.append(0)
        continue
    """
将i插入
然后排序
找到index(i)
跟前面一个
后面一个进行比较选择最小的值
如果在第一个位置或者最后一个位置特殊处理
然后将i移除
一下还要
abs....

而且要考虑
loc_c - 2
这个会不会越界
前面要单独判断

这个算法不好
参考一下别人的
"""
loc_C.append(i)
loc_C.sort()
loc_i = loc_C.index(i)
if loc_i == 0:
    loc.append(loc_C[1]-i)
elif loc_i == len(loc_C) - 1:
    loc.append(loc_C[len(loc_C) - 2]-i)
else:
    loc.append(min(loc_C[loc_i - 1], loc_C[loc_i + 1])-i)
loc_C.remove(i)

return loc

"""


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        # 跟我的思路一样 不过我没处理好 后面的部分
        import re
        loc = [m.start() for m in re.finditer(C, S)]  # 寻找所在位置
        distance = []
        for i in range(len(S)):
            distance.append(min([abs(x - i) for x in loc]))

        return distance


def main():
    result = Solution().shortestToChar(S="loveleetcode", C='e')
    print(result)
    return result


if __name__ == "__main__":
    main()
