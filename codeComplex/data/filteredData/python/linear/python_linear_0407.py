import random

def main(n: int):
    # 生成规模为 n 的测试数据
    # N: 使用 n
    N = n

    # M: 生成一个正浮点数，避免太小
    M = random.uniform(1.0, 100.0)

    # A: 长度 N 的正整数列表
    A = [random.randint(1, 10) for _ in range(N)]

    # B: 长度 N 的整数列表，避免后续 C 中出现 1 以防止除零
    # 因为后面有 M/(c-1)，若 c=1 则除以 0
    B = [random.randint(2, 10) for _ in range(N)]

    # 原逻辑开始
    B_rot = B[1:] + [B[0]]
    C = []
    for a, b in zip(A[::-1], B_rot[::-1]):
        C.append(b)
        C.append(a)

    if 1 in C:
        print(-1)
        return

    M0 = M
    for c in C:
        # 若生成数据导致 c == 1，会出现除零，这里加防御
        if c == 1:
            print(-1)
            return
        M += M / (c - 1)

    print(M - M0)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)