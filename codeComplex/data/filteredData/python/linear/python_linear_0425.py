import random

def main(n):
    # 生成测试数据：随机选择 x，生成 n 个整数放入集合 a
    # 可以根据需要调整数据范围
    x = random.randint(1, 10**9)
    # 为避免 a 的去重导致规模 < n，这里生成 2n 个数再取前 n 个不同的
    nums = [random.randint(0, 10**9) for _ in range(2 * n)]
    a = []
    seen = set()
    for v in nums:
        if v not in seen:
            seen.add(v)
            a.append(v)
            if len(a) == n:
                break
    a = set(a)

    # 原逻辑开始
    if len(a) < n:
        print(0)
    else:
        d = set()
        p = 0
        for i in a:
            val = i & x
            d.add(val)
            if val != i and val in a:
                print(1)
                p = 1
                break
        if len(d) < n and p == 0:
            print(2)
        elif p != 1:
            print(-1)

if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(5)