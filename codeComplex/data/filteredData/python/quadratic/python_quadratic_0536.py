import sys
import math
import collections
import bisect
import atexit

sys.setrecursionlimit(1000000)

try:
    import numpy  # noqa: F401

    def dprint(*args, **kwargs):
        # print(*args, file=sys.stderr)
        pass
    dprint('debug mode')
except Exception:  # pragma: no cover
    def dprint(*args, **kwargs):
        pass


MAXN = 10**18 + 10


def getUpper(N):
    z = 1
    r = 0
    for _ in range(N):
        r += z
        z *= 4
        if r > MAXN:
            break
    return r


def solve_case(N, K):
    tk = K
    z = 1
    for _ in range(N):
        tk -= z
        z *= 4
        if tk < 0:
            break
    if tk > 0:
        return "NO"

    nowcut = 0
    nt = 1
    nowupper = 0
    ok = False
    idx = -1

    for i in range(N):
        nt *= 2
        nowcut += nt - 1

        if nowcut > K:
            break
        t = (nt * 2 - 3)
        tu = t * getUpper(N - 1 - i)
        nowupper += tu
        dprint('bound', nowcut, nowcut + nowupper)
        if nowcut <= K <= nowcut + nowupper:
            ok = True
            idx = N - 1 - i
            break

    if ok:
        return f"YES {idx}"

    else:
        return "NO"


def generate_test_data(n):
    """
    根据规模 n 生成 (T, [(N, K), ...]) 测试数据：
    - T: 测试用例数量
    - 每个用例为一个 (N, K) 元组
    """
    # 这里给出一种简单的构造方式，可以按需要调整：
    # 令 T = n，N 在 [1, max(1, n//2)] 范围内变化，
    # K 在 [0, getUpper(N)] 范围内取一些代表值。
    cases = []
    T = n

    maxN = max(1, n // 2)
    for i in range(1, T + 1):
        N = 1 + (i % maxN)  # N 至少为 1
        upper = getUpper(N)
        # 选取几种不同类型的 K：
        if i % 3 == 0:
            K = 0
        elif i % 3 == 1:
            K = min(upper, i)  # 较小的 K

        else:
            K = min(upper, upper // 2 + i)  # 中等偏大的 K
        cases.append((N, K))

    return T, cases


def main(n):
    """
    根据规模 n 生成测试数据并执行原有逻辑，将结果打印到标准输出。
    """
    T, cases = generate_test_data(n)

    for N, K in cases:
        res = solve_case(N, K)
        # print(res)
        pass
if __name__ == "__main__":
    # 示例：可以在这里手动指定规模进行快速运行
    main(100)