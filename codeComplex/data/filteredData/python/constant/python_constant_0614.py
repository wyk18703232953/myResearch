from math import sin, tan, cos, pi, atan2, sqrt, acos, atan, factorial
import random


def get(l, r):
    if l > r:
        return 0

    if l & 1:
        return (-l - r) * (r - l + 2) // 4
    else:
        return (l + r) * (r - l + 2) // 4


def solution(l, r):
    l1, l2, r1, r2 = l, l, r, r

    if l & 1:
        l2 += 1
    else:
        l1 += 1

    if r & 1:
        r2 -= 1
    else:
        r1 -= 1

    return get(l1, r1) + get(l2, r2)


def main(n):
    # 生成 n 组测试数据 (l, r)，保证 1 <= l <= r <= 10^9
    q = n
    test_cases = []
    for _ in range(q):
        l = random.randint(1, 10**9 - 1)
        r = random.randint(l, 10**9)
        test_cases.append((l, r))

    # 输出结果
    for l, r in test_cases:
        print(solution(l, r))


if __name__ == "__main__":
    # 示例：运行 main(5) 进行 5 组随机测试
    main(5)