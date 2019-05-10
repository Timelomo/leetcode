"""
0 <= bills.length <= 10000
bills[i] 不是 5 就是 10 或是 20

1. 如果[xxx] 里面的第一个不是 5 直接 false

如果是5 的话直接收入
如果是10 的话 收入中减 5  并将10 收入
如果是20 的话 优先收入减少10 然后再考虑5

如果不能够满足找零 直接false

"""


class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if bills and bills[0] != 5:
            return False

        wallet = []

        for i in range(len(bills)):
            if bills[i] == 5:
                wallet.append(5)

            elif bills[i] == 10:
                wallet.append(10)
                if 5 not in wallet:
                    return False
                wallet.remove(5)

            else:
                if wallet.count(5) >= 3 or (wallet.count(10) >= 1 and wallet.count(5) >= 1):
                    if wallet.count(10) >= 1 and wallet.count(5) >= 1:
                        wallet.remove(10)
                        wallet.remove(5)
                    else:
                        wallet.remove(5)
                        wallet.remove(5)
                        wallet.remove(5)
                else:
                    return False

        return True


def main():
    # result = Solution().lemonadeChange([5, 5, 5, 10, 20])
    # result = Solution().lemonadeChange([5, 5, 10])
    # result = Solution().lemonadeChange([5, 10, 10])
    result = Solution().lemonadeChange([5, 5, 5, 10, 5, 5, 10, 20, 20, 20])
    print(result)
    return result


if __name__ == '__main__':
    main()
