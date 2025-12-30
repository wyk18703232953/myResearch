import random

def main(n):
    # n：要生成的查询数量 q
    q = n
    print("q =", q)
    
    # 随机生成 q 组 (l, r)，保持 l <= r
    queries = []
    for _ in range(q):
        l = random.randint(1, 10**6)
        r = random.randint(l, l + random.randint(0, 10**6))
        queries.append((l, r))

    # 输出测试数据（可选：如果只要结果，可以去掉这段打印）
    print("Generated queries (l, r):")
    for l, r in queries:
        print(l, r)
    
    # 原逻辑计算并输出结果
    print("Results:")
    for l, r in queries:
        sign = -1 if l % 2 else 1
        if (r - l) % 2:
            print(-sign * (r - l + 1) // 2)
        else:
            print(sign * (l + (r - l) // 2))


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)