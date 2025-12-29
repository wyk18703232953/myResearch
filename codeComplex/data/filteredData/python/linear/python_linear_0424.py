import sys
import math
import random

def main(n: int):
    # 生成测试数据
    # 约定：
    #   a = n
    #   b 在 [0, 2^17-1] 范围内随机生成（保证不超过 t 的长度）
    #   l[i] 在 [0, 100000] 范围内随机生成
    a = n
    b = random.randint(0, (1 << 17) - 1)
    l = [random.randint(0, 100000) for _ in range(a)]

    # 原始逻辑开始
    t = [[-1, 0] for _ in range(100001)]
    for i in range(a):
        if t[l[i]][0] != -1:
            print(0)
            return
        t[l[i]][0] = 3

    s = math.inf
    for i in range(a):
        idx = l[i] & b
        if idx <= 100000 and t[idx][0] != -1:
            if idx != l[i] and t[idx][0] != 1:
                t[idx] = [1, min(2, t[idx][1] + 1)]
        elif idx <= 100000:
            t[idx] = [2, 1]
        # 如果 (l[i] & b) > 100000，原代码会越界，这里简单跳过

    for i in range(a):
        idx = l[i] & b
        if idx <= 100000 and t[idx][1] != 0 and t[idx][0] == 1:
            s = min(s, t[idx][1])

    if s == math.inf:
        print(-1)
    else:
        print(s)


if __name__ == "__main__":
    # 示例：运行规模 n = 10，可根据需要修改
    main(10)