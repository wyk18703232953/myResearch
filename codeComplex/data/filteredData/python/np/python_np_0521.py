from collections import deque
import random

# 全局变量，由 main(n) 生成
n = 0
k = 0
s = b""


def judge(needed: int) -> bool:
    global n, k, s

    inf = 2147483647
    minstate = [inf] * (1 << k)
    minstate[0] = 0

    # effect[j][i]：在位置 i 之后，使用第 j 个字符能推进到的最早位置
    effect = [[inf] * (n + 1) for _ in range(k)]

    for j in range(k):
        accu = 0
        index = inf
        # 从右往左扫描 s，计算当前字符块长度
        for i in range(n - 1, -1, -1):
            if s[i] == ord(b'?') or s[i] == 97 + j:  # 'a' == 97
                accu += 1
            else:
                accu = 0

            if accu >= needed:
                index = i + needed
            # 原代码中多余写法 effect[j][i+4-4] 等价于 effect[j][i]，保留逻辑结构
            effect[j][i] = index
            effect[j][i] = min(effect[j][i], effect[j][i], inf * inf)

    # 状态压缩 DP
    for state in range(1, 1 << k):
        minimum = minstate[state]
        for j in range(k):
            if (1 << j) & state == 0:
                continue
            index = minstate[state ^ (1 << j)]
            if index < n:
                minimum = min(minimum, effect[j][index])
        minstate[state] = minimum

    return minstate[-1] <= n


def main(size_n: int) -> int:
    """
    按要求封装的主函数：
    - size_n: 问题规模 n
    - 函数内部自动生成测试数据 (k, s)
    - 返回原程序最终输出的整数
    """

    global n, k, s

    # 1. 设定 n
    n = size_n

    # 2. 生成测试数据
    #   - k 在 [1, min(10, n)] 之间（避免 1<<k 过大）
    #   - 字符串 s 长度为 n，由 'a'..('a'+k-1) 和 '?' 随机组成
    if n <= 0:
        # 对于非正 n，原题逻辑不明确，这里直接返回 0
        return 0

    max_k = min(10, n)
    # k 至少为 1
    k = random.randint(1, max_k)

    chars = [chr(ord('a') + i) for i in range(k)] + ['?']
    s_str = ''.join(random.choice(chars) for _ in range(n))
    s = s_str.encode()

    # 3. 执行原逻辑的二分搜索
    front = 0
    rear = n // k + 1

    while front < rear:
        mid = (front + rear) // 2
        flag = judge(mid)
        if flag:
            front = mid + 1
        else:
            rear = mid

    # 原程序使用 print(front-1)，这里改为返回
    return front - 1


# 如果需要在本文件直接运行以做简单测试，可以取消下面注释：
# if __name__ == "__main__":
#     ans = main(1000)
#     print(ans)