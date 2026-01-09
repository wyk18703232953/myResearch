import sys
import math
import collections
import bisect

sys.setrecursionlimit(1000000)


def dprint(*args, **kwargs):
    # 调试输出，如需调试可取消注释下一行
    # print(*args, file=sys.stderr)
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


def solve_one(N, K):
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
    depth_ans = -1

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
            depth_ans = N - 1 - i
            break

    if ok:
        return f"YES {depth_ans}"

    else:
        return "NO"


def main(n):
    """
    n 为规模参数，用来生成 T 组测试数据。
    这里的策略：
      - T = n
      - 对于第 i 组：N = i + 1
      - K 取一个在 0 到 getUpper(N) 之间的值（简单取 min(i, getUpper(N))）
    """
    T = n
    results = []

    for i in range(T):
        N = i + 1
        upper = getUpper(N)
        K = min(i, upper)  # 简单构造一个不太大的 K
        res = solve_one(N, K)
        results.append((N, K, res))

    # 输出格式：每行：N K 结果
    for N, K, res in results:
        # print(N, K, res)
        pass
if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)