def main(n: int):
    # 根据规模 n 生成一组 (N, K) 测试数据
    # 此处简单构造：N = n，K 在 {1, 3, N//2, N-1} 中选一个
    N = n
    if N <= 1:
        K = 1
    elif N == 2:
        K = 1
    elif N == 3:
        K = 3
    else:
        # 简单规则：根据 n 的模来切换几种情况
        r = N % 4
        if r == 0:
            K = 1
        elif r == 1:
            K = 3 if N >= 4 else 1
        elif r == 2:
            K = N // 2
        else:
            K = N - 1

    if N == K:
        print("0" * N)
    elif K == 1:
        print("0" * (N - 1) + "1")
    elif K == 3:
        # 当 N<4 时，原逻辑 "1" + "0"*(N-4) + "101" 不合理，这里做个保护
        if N < 4:
            # 回退到 K==1 的情况
            print("0" * (N - 1) + "1")
        else:
            print("1" + "0" * (N - 4) + "101")
    else:
        res = ["0"] * N
        step = N // 2 - K // 2 + 1
        if step <= 0:
            step = 1  # 防御性处理，避免死循环或异常步长
        for i in range(0, N, step):
            res[i] = "1"
        print(''.join(res))


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)