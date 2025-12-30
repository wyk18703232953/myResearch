from math import sqrt
import random

def findt(u, v, a, dist):
    front = (v * v - u * u) / (2 * a)
    if front > dist:
        return (sqrt(u * u + 2 * a * dist) - u) / a
    return (v - u) / a + (dist - front) / v


def solve(a, v, l, d, w):
    if v <= w or 2 * a * d <= w * w:
        return findt(0, v, a, l)
    after = findt(w, v, a, l - d)
    peak = sqrt(a * d + w * w / 2)
    if peak > v:
        travel = (v * v - w * w / 2) / a
        before = (2 * v - w) / a + (d - travel) / v
    else:
        before = (2 * peak - w) / a
    return before + after


def generate_test_case(n):
    # n 用作放大参数，生成一组合理的 (a, v, l, d, w)
    # 控制范围：加速度 1~n，速度与距离随 n 增大
    a = random.randint(1, max(1, n))
    v = random.randint(1, max(1, 5 * n))
    l = random.randint(1, max(1, 10 * n))
    d = random.randint(1, max(1, l))  # d 不超过 l
    w = random.randint(0, max(1, 5 * n))
    return a, v, l, d, w


def main(n):
    a, v, l, d, w = generate_test_case(n)
    result = solve(a, v, l, d, w)
    print(f"{result:.8f}")


if __name__ == "__main__":
    # 示例：使用 n=10 运行
    main(10)