from collections import deque
import random

def main(n):
    # 生成测试数据
    # n 为序列长度，构造 1..n 的随机排列，保证元素互不相同
    a = deque(random.sample(range(1, 10 * n + 1), n))

    # 生成查询次数 q，并随机生成 q 个查询
    q = max(1, n * 2)  # 可按需调整规模关系
    queries = [random.randint(1, 10 ** 9) for _ in range(q)]

    # 原逻辑开始
    b = []
    m = a.index(max(a))

    for _ in range(m):
        a0, a1 = a.popleft(), a.popleft()
        b.append([a0, a1])
        if a0 < a1:
            a0, a1 = a1, a0
        a.appendleft(a0)
        a.append(a1)

    # 输出结果
    for c in queries:
        if c <= m:
            print(f"{b[c-1][0]} {b[c-1][1]}")
        else:
            c -= m + 1
            c %= n - 1
            print(f"{a[0]} {a[c+1]}")

if __name__ == "__main__":
    # 可以在此处指定 n 的大小进行测试
    main(5)