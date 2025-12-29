import random

def main(n: int):
    # 生成测试数据：
    # 为了尽量保证有解，先生成 A, B，再生成不超过 min(A,B) 的 C，
    # 最后 N 在 [A + B - C + 1, A + B - C + n] 中取值（保证 D > 0）。
    A = random.randint(1, n)
    B = random.randint(1, n)
    C = random.randint(0, min(A, B))
    base = A + B - C
    N = base + random.randint(1, max(1, n))  # 保证 N > base，从而 D > 0

    D = N - (A + B - C)
    if D <= 0 or C > A or C > B:
        print('-1')
        return
    print(D)


if __name__ == "__main__":
    # 示例：规模取 100，可按需修改
    main(100)