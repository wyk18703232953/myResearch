import random

def solve_case(n, m, k):
    if k == 0:
        if n == 0 and m == 0:
            return 0
        else:
            return -1
    elif k == 1:
        if max(abs(n), abs(m)) != 1:
            return -1
        elif abs(n) == abs(m) == 1:
            return 1
        else:
            return 0
    else:
        if max(abs(n), abs(m)) > k:
            return -1
        elif abs(n) == abs(m):
            if (k - abs(n)) % 2 == 0:
                return k
            else:
                return k - 2
        elif (max(abs(n), abs(m)) - min(abs(n), abs(m))) % 2 == 0:
            if (k - max(abs(n), abs(m))) % 2 == 0:
                return k
            else:
                return k - 2
        else:
            return k - 1

def main(n):
    # n: 规模，用作测试用例数量 q
    q = n
    random.seed(0)

    tests = []
    for _ in range(q):
        # 生成测试数据：n, m 在 [-n, n] 范围内，k 在 [0, 2n] 范围内
        nn = random.randint(-n, n)
        mm = random.randint(-n, n)
        kk = random.randint(0, 2 * max(1, n))
        tests.append((nn, mm, kk))

    for nn, mm, kk in tests:
        print(solve_case(nn, mm, kk))

if __name__ == "__main__":
    # 示例：规模 5
    main(5)