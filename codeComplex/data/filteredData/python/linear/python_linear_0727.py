def main(n):
    # 映射 n 为原程序的 N 和 K
    # 为了可规模化和覆盖不同分支，这里设定：
    # N = max(1, n)
    # K 在 [1, N] 内按确定性规则变化
    N = max(1, n)
    if N == 1:
        K = 1
    else:
        # 让 K 在 1..N 之间循环变化，且避免为 0
        K = (n % N) + 1

    if N == K:
        print("0" * N)
    elif K == 1:
        print("0" * (N - 1) + "1")
    elif K == 3:
        if N >= 4:
            print("1" + "0" * (N - 4) + "101")
        else:
            # 原逻辑在 N < 4 且 K == 3 时会构造负长度字符串
            # 这里按最接近的行为处理为全 1，保持确定性
            print("1" * N)
    else:
        res = ["0"] * N
        step = N // 2 - K // 2 + 1
        if step <= 0:
            step = 1
        for i in range(0, N, step):
            res[i] = "1"
        print(''.join(res))


if __name__ == "__main__":
    # 示例：运行若干不同规模
    for n in [1, 2, 3, 4, 5, 10, 20]:
        main(n)