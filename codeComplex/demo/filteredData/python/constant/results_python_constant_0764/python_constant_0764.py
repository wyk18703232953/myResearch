import math

def main(n):
    # 映射：给定规模 n，构造一对 (N, K)
    # 保证随 n 增大而整体规模增大，且完全确定
    N = n
    K = n * n

    q = int(-3 + math.sqrt(9 + 8 * (N + K))) // 2
    r = N - q
    # print(r)
    pass
if __name__ == "__main__":
    main(10)