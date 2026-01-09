import sys
import math
from collections import defaultdict, deque

def main(n):
    # 数据生成：长度为 n 的字符串 s 和 t
    # s 为按字母循环递增生成
    # t 为 s 的一个可通过相邻交换得到的排列
    alphabet = [chr(ord('a') + (i % 26)) for i in range(n)]
    s = alphabet[:]  # 原始字符串
    t = alphabet[::-1]  # 生成一个固定的目标排列（反转），保证可通过相邻交换得到

    s = list(s)
    t = list(t)

    res = True
    ans = []
    for i in range(n):
        if s[i] == t[i]:
            continue

        else:
            ind = -1
            for j in range(i + 1, n):
                if t[i] == s[j]:
                    ind = j
                    break
            if ind == -1:
                res = False
                break
            for j in range(ind - 1, i - 1, -1):
                ans.append(j + 1)
                s[j], s[j + 1] = s[j + 1], s[j]

    if res:
        # print(len(ans))
        pass

        if ans:
            # print(*ans)
            pass

        else:
            # print()
            pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    main(10)