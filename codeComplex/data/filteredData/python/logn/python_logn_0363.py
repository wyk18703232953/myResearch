mod = 10**9 + 7

def main(n):
    # 1. 生成规模为 n 的测试数据（这里简单设定 x = n, k = n^2 作为示例）
    x = n
    k = n * n

    # 2. 保留原有逻辑
    if x == 0:
        print(0)
        return

    # 预计算 2^i (mod)，长度仍按原程序 1024
    T = [1]
    for _ in range(1024):
        T.append((2 * T[-1]) % mod)

    # 预计算 (2^1024)^i (mod)，长度仍按原程序 10**6
    L = [1]
    for _ in range(10**6):
        L.append((T[1024] * L[-1]) % mod)

    k = k % (mod - 1)

    t1 = k % 1024
    t2 = (k + 1) % 1024

    q1 = k // 1024
    q2 = (k + 1) // 1024

    A = (L[q2] * T[t2]) % mod
    A *= x
    A %= mod

    B = (L[q1] * T[t1]) % mod

    print((A - B + 1) % mod)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需调整
    main(10)