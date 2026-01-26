def main(n):
    # 这里将 n 映射为网格的规模：n -> n 行 n 列
    # 若需要其他映射方式，可自行修改为 (n, 2*n) 等
    if n <= 0:
        return

    N = n
    M = n

    for i in range(1, N // 2 + 1):
        for j in range(1, M + 1):
            # print(f"{i} {j}")
            pass
            # print(f"{N - i + 1} {M - j + 1}")
            pass
    if N % 2 == 1:
        mid_row = N // 2 + 1
        for j in range(1, M // 2 + 1):
            # print(f"{mid_row} {j}")
            pass
            # print(f"{mid_row} {M - j + 1}")
            pass
        if M % 2 == 1:
            # print(f"{mid_row} {M // 2 + 1}")
            pass
if __name__ == "__main__":
    # 示例调用：可按需要修改 n 的规模
    main(5)