import random

def main(n):
    # 生成测试数据：q 次操作，每次随机一个 u 和一个操作串 s
    # 为了规模感明显，令 q 与 n 同阶（可按需调整）
    q = min(n, 10**5)  # 防止过大
    queries = []
    for _ in range(q):
        u = random.randint(1, n)
        # 操作串长度在 1 到 20 之间
        length = random.randint(1, 20)
        # 操作由 'L', 'R', 'U' 组成
        s = ''.join(random.choice('LRU') for _ in range(length))
        queries.append((u, s))

    # 原逻辑
    for u, s in queries:
        for comm in s:
            k = 1
            while True:
                if k & u:
                    break
                k <<= 1
            if comm == 'L':
                if k != 1:
                    u -= k
                    u += (k >> 1)
            elif comm == 'R':
                if k != 1:
                    u += (k >> 1)
            elif comm == 'U':
                nu = u - k
                nu |= (k << 1)
                if nu <= n:
                    u = nu
        print(u)


if __name__ == "__main__":
    # 示例运行：可根据需要修改 n
    main(10**6)