import random


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
    b = [(a[i], t[i], i + 1) for i in range(n)]
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
    # 随机设置 T，a[i]，t[i]，可按需要调整生成规则
    random.seed(0)
    # 让时间上限和 t 的数量级匹配
    T = random.randint(max(1, n // 2), max(1, 3 * n))

    a = [random.randint(1, n) for _ in range(n)]
    t = [random.randint(1, 10) for _ in range(n)]

    point, probs = solve(n, T, a, t)

    print(point)
    print(len(probs))
    if probs:
        print(" ".join(str(x) for x in probs))


if __name__ == "__main__":
    # 示例：可根据需要调整 n
    main(10)