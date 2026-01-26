import math

def core_logic(N, K):
    n = (-3 + math.sqrt(9 + 4 * (2 * N + 2 * K))) / 2
    return int(N - n)

def main(n):
    if n <= 0:
        return 0
    # 将 n 映射为 (N, K)，保证可规模化且确定性
    N = n * (n + 1) // 2
    K = n * (n - 1) // 2
    result = core_logic(N, K)
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)