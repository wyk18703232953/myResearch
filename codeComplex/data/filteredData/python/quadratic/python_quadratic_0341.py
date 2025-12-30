import sys
import math
import random
from collections import defaultdict, deque


def main(n: int):
    # 生成测试数据：随机生成两个长度为 n 的小写字母串 s 和 t
    # 为了增加成功概率，让 t 成为 s 的随机打乱版（可通过相邻交换实现）
    letters = [chr(ord('a') + i) for i in range(3)]  # 使用较少字符，方便出现差异
    s = [random.choice(letters) for _ in range(n)]
    # 为保证 t 可以通过相邻交换得到，这里直接打乱 s 的拷贝
    t = s[:]
    random.shuffle(t)

    s = s[:]  # 工作副本
    t = t[:]

    res = True
    ans = []

    # 原逻辑：通过相邻交换把 s 变成 t，记录交换位置
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
        print(len(ans))
        if ans:
            print(*ans)
        else:
            # 为保持输出格式，当没有操作时只输出 0 一行
            pass
    else:
        print(-1)


if __name__ == '__main__':
    # 示例：可以在这里手动设置 n 的规模进行测试
    main(5)