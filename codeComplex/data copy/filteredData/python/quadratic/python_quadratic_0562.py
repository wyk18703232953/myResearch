import sys

def generate_input(n):
    # 将 n 映射为 N 和 M，使得规模约为 n
    # 这里选择 N = n, M = n，使得总规模为 n^2
    if n <= 0:
        return 1, 1
    N = n
    M = n
    return N, M

def core_logic(N, M):
    Ans = [(0, 0) for _ in range(N * M)]
    for i in range(1, N * M + 1):
        if i % 2:
            a, b = divmod(i // 2, M)

        else:
            a, b = divmod(N * M - i // 2, M)
        Ans[i - 1] = (a + 1, b + 1)
    return Ans

def main(n):
    N, M = generate_input(n)
    ans = core_logic(N, M)
    out_lines = ["{} {}".format(a, b) for a, b in ans]
    sys.stdout.write("\n".join(out_lines) + ("\n" if out_lines else ""))

if __name__ == "__main__":
    # 示例：使用 n = 3 运行
    main(3)