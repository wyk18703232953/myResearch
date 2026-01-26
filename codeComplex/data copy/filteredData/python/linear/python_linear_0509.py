import math
import sys

sys.setrecursionlimit(1000000)


def main(n):
    # 映射：n 作为字符串长度 N
    N = max(1, n)

    # 构造两个确定性的长度为 N 的二进制字符串
    # s1: 0101...
    s1 = ''.join('0' if i % 2 == 0 else '1' for i in range(N)) + '0'
    # s2: 1010...
    s2 = ''.join('1' if i % 2 == 0 else '0' for i in range(N)) + '0'

    res = 0
    i = 0
    while i < N:
        if s1[i] != s2[i]:
            if s1[i + 1] == s2[i] and s2[i + 1] == s1[i]:
                res += 1
                i += 2
                continue
            res += 1
        i += 1
    # print(res)
    pass
if __name__ == "__main__":
    main(10)