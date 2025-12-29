import random

def main(n):
    # 生成测试数据
    # 数组 a 的元素范围可以自行调整，这里设为 1..10^9
    a = [random.randint(1, 10**9) for _ in range(n)]
    # 生成 m：这里设为 n（可根据需要调整规则）
    m = n
    queries = []
    for _ in range(m):
        l = random.randint(1, n)
        r = random.randint(1, n)
        if l > r:
            l, r = r, l
        queries.append((l, r))

    # 下面是原始逻辑（移除 input，直接使用生成的数据）
    parity = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[j] < a[i]:
                parity ^= 1

    for l, r in queries:
        dist = (r - l + 1)
        pairs = (dist - 1) * dist // 2

        if pairs & 1:
            parity ^= 1

        if parity:
            print("odd")
        else:
            print("even")


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行修改
    main(5)