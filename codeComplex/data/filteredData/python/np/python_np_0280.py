import random

def main(n: int):
    # 生成测试数据：q 个查询
    # 这里设定 q 与 n 同阶，例如 q = n（可根据需要调整）
    q = max(1, n)
    
    queries = []
    for _ in range(q):
        # u 在 [1, n] 内随机
        u = random.randint(1, n)
        # 操作串长度：设为 1 ~ 20 之间的随机长度（可按需要调整）
        length = random.randint(1, 20)
        s = ''.join(random.choice('LRU') for _ in range(length))
        queries.append((u, s))

    # 按原逻辑处理并输出结果
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
    # 示例：调用 main(10)
    main(10)