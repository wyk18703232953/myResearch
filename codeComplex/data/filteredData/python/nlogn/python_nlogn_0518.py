import random
import math


def process(A):
    d = {}
    final = set()
    for x in A:
        if x not in d:
            d[x] = 0
        d[x] += 1
        if d[x] >= 4:
            return [x, x, x, x]
        if d[x] >= 2:
            final.add(x)
    L = sorted(final)
    answer = [float('inf'), None, None]
    for i in range(len(L) - 1):
        a = L[i]
        b = L[i + 1]
        a1 = a / b + b / a
        answer = min(answer, [a1, a, b])
    a1, a, b = answer
    return [a, a, b, b]


def main(n):
    """
    n: 规模参数，这里视为每个测试中的数组长度
    自动生成测试数据并运行原逻辑。
    """
    random.seed(0)

    # 生成 t 个测试，每个测试长度为 n
    t = 5
    tests = []
    for _ in range(t):
        # 元素取值范围可以根据需要调整
        # 为了保证出现重复，从较小范围取值
        A = [random.randint(1, max(2, n // 2)) for _ in range(n)]
        tests.append(A)

    for A in tests:
        a, b, c, d = process(A)
        print(f"{a} {b} {c} {d}")


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)