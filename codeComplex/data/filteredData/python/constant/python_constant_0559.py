import random

def main(n: int):
    # 1. 生成测试数据：根据规模 n 构造 n, m, k, l
    # 为了保持逻辑合理性，确保:
    #   1 <= m <= n
    #   0 <= k <= n
    #   0 <= l <= n
    # 其余随机生成
    N = n
    m = random.randint(1, max(1, N))
    k = random.randint(0, N)
    l = random.randint(0, N)

    # 原始逻辑开始
    if l > N - k:
        print(-1)
    else:
        am = ((l + k) // m + bool((l + k) % m))
        if am * m > N:
            print(-1)
        else:
            print(am)

if __name__ == "__main__":
    # 可在此处修改规模 n
    main(10)