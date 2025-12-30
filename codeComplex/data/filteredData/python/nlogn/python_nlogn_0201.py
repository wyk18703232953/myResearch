from random import randint


def check(k, b, T):
    c = [e for e in b if e[0] >= k]

    if len(c) < k:
        return False, None

    first_k_probs = c[:k]
    s = sum(e[1] for e in first_k_probs)

    if s > T:
        return False, None

    return True, first_k_probs


def solve(n, T, a, t):
    b = []

    for i in range(n):
        b.append((a[i], t[i], i + 1))

    b.sort(key=lambda x: x[1])

    low, high = 0, n
    result = 0
    final_probs = []

    while low <= high:
        mid = (low + high) // 2

        possible, probs = check(mid, b, T)
        if possible:
            result, final_probs = mid, probs
            low = mid + 1
        else:
            high = mid - 1

    return result, [e[2] for e in final_probs]


def main(n):
    # 生成测试数据
    # 约定：
    #   a[i] ∈ [1, n] 表示题目难度或分值
    #   t[i] ∈ [1, n] 表示所需时间
    #   T 为总时间上限，简单设置为 n 的若干倍
    T = 2 * n
    a = [randint(1, n) for _ in range(n)]
    t = [randint(1, n) for _ in range(n)]

    point, probs = solve(n, T, a, t)

    # 按原程序的输出格式打印
    print(point)
    print(len(probs))
    if probs:
        print(" ".join(str(x) for x in probs))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)