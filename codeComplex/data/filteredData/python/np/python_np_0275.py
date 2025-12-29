import sys
import math
import random

MOD = 10**9 + 7
sys.setrecursionlimit(1000000)

def hgt(x, N):
    if x == 0:
        return -1
    h = 0
    while x & 1 != 1:
        h += 1
        x = x >> 1
    return h

def up(x, N):
    h = hgt(x, N)
    g = x + (1 << h)
    if g > 0 and g < N and hgt(g, N) == h + 1:
        return g
    g = x - (1 << h)
    if g > 0 and g < N and hgt(g, N) == h + 1:
        return g
    return x

def left(x, N):
    h = hgt(x, N)
    if h == 0:
        return x
    g = x - (1 << (h - 1))
    if g > 0:
        return g
    return x

def right(x, N):
    h = hgt(x, N)
    if h == 0:
        return x
    g = x + (1 << (h - 1))
    if g < N:
        return g
    return x

def main(n):
    """
    n: 规模参数，用来控制 N 和查询数量 q 的大小。
    测试数据生成规则（可根据需要调整）：
      - N = n + 1（原程序中会对输入的 N 做 N += 1）
      - q = n
      - p 随机生成于 [1, N-1]
      - 每个操作串长度在 [1, max(1, n // 2)]，字符从 'U', 'L', 'R' 中随机生成
    """
    global_N = n + 1
    q = n

    outputs = []

    for _ in range(q):
        p = random.randint(1, global_N - 1)
        # 控制操作串长度，防止规模过大
        max_len = max(1, n // 2)
        length = random.randint(1, max_len)
        ops = ''.join(random.choice('ULR') for _ in range(length))

        for c in ops:
            if c == 'U':
                p = up(p, global_N)
            elif c == 'R':
                p = right(p, global_N)
            else:  # 'L'
                p = left(p, global_N)
        outputs.append(str(p))

    # 输出所有结果
    sys.stdout.write("\n".join(outputs))

# 示例调用（提交到评测系统时可注释掉）
# if __name__ == "__main__":
#     main(10)