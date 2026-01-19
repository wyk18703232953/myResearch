import sys
from collections import deque

def build_input(n):
    # 将 n 映射到字符串长度和字母种类 k
    # 这里选择：字符串长度 = n，k = 3（可根据需要调整）
    if n < 1:
        n = 1
    k = 3
    # 构造一个确定性的带 '?' 的字符串模式
    # 模式：循环 'a','b','c','?'，长度为 n
    base_chars = [ord('a') + i for i in range(k)]  # a,b,c
    res = []
    for i in range(n):
        t = i % (k + 1)
        if t < k:
            res.append(base_chars[t])
        else:
            res.append(ord('?'))
    s_bytes = bytes(res)
    return n, k, s_bytes

def judge(n, k, s, needed):
    inf = 2147483647
    minstate = [inf] * (1 << k)
    minstate[0] = 0

    effect = [[inf] * (n + 1) for _ in range(k)]

    for j in range(k):
        accu = 0
        index = inf
        for i in range(n - 1, -1, -1):
            if s[i] == ord('?') or s[i] == 97 + j:
                accu += 1
            else:
                accu = 0
            if accu >= needed:
                index = i + needed
            effect[j][i] = index
            # 原代码里这行写法有冗余的加减法，但逻辑等价于：
            effect[j][i] = min(effect[j][i], effect[j][i + 1] if i + 1 <= n else inf, inf * inf)

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

def core(n, k, s):
    front = 0
    rear = n // k + 1
    while front < rear:
        mid = (front + rear) // 2
        flag = judge(n, k, s, mid)
        if flag:
            front = mid + 1
        else:
            rear = mid
    return front - 1

def main(n):
    n_in, k_in, s_in = build_input(n)
    ans = core(n_in, k_in, s_in)
    print(ans)

if __name__ == "__main__":
    main(1000)