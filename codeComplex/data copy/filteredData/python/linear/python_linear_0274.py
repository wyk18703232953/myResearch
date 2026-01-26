def main(n):
    # 对于原程序，输入为单组：n, m, a, b
    # 将规模参数 n 解释为：m = n，a = n // 2，b = n // 3
    # 为避免 m 为 0 时取模错误，当 n <= 0 时直接返回 0
    if n <= 0:
        # print(0)
        pass
        return

    N = n
    M = n
    A = n // 2
    B = n // 3

    # 保持原逻辑：n,m,a,b=map(int,input().split())
    # print(min(n%m*b, (m-n%m)*a))
    result = min(N % M * B, (M - N % M) * A)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：可按需修改 n 来做规模实验
    main(10)