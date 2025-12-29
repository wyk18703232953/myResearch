import random

def main(n):
    # 生成 n 组测试数据 (l, r)，保证 l <= r 且为正整数
    queries = []
    for _ in range(n):
        l = random.randint(1, 10**6)
        r = random.randint(l, l + 10**6)
        queries.append((l, r))

    for l, r in queries:
        if l % 2 == 0:
            count = -((r - l + 1) // 2)
        else:
            count = ((r - l + 1) // 2)
        if (r - l + 1) % 2 == 0:
            print(count)
        else:
            if r % 2 == 0:
                print(count + r)
            else:
                print(count - r)

if __name__ == "__main__":
    # 示例：运行规模 n=5
    main(5)