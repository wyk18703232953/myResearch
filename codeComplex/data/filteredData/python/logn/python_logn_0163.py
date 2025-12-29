import random

def main(n: int):
    # 根据规模 n 生成测试数据：
    # 这里假设 n 控制 N 的大小，K 与 N 同数量级
    # 你可根据实际需求调整数据生成策略
    N = random.randint(1, max(1, n))
    K = random.randint(1, max(1, n))

    def in_bounds(k: int) -> bool:
        # 使用外部作用域中的 N, K
        return N <= K * (K + 1) // 2 - (K - k) * (K - k + 1) // 2 - k + 1

    l = 0
    r = K
    while l <= r:
        c = (l + r) // 2
        if in_bounds(c):
            r = c - 1
        else:
            l = c + 1

    if in_bounds(K):
        print(l)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：规模取 100，可自行修改或在外部调用 main(n)
    main(100)