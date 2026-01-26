import sys

INF = 10**9 + 7
sys.setrecursionlimit(INF)


def fo(*args):
    out = []
    for s in args:
        out.append(str(s))
    sys.stdout.write(" ".join(out) + "\n")


def mask(n1):
    arr = []
    for _ in range(64):
        arr.append(n1 & 1)
        n1 >>= 1
    arr.reverse()
    return arr


def getn(mask_arr):
    if sum(mask_arr) == 0:
        return 0
    res = 0
    for i in range(63, -1, -1):
        res += (2 * mask_arr[i]) ** (63 - i)
    return res


def solve(n1, n2):
    m1 = mask(n1)
    m2 = mask(n2)

    sol = [0 for _ in range(64)]

    for i in range(64):
        if m1[i] != m2[i]:
            sol[i] = 1
            break

    i += 1
    for j in range(i, 64):
        sol[j] = 1

    res = getn(sol)
    return res


def main(n):
    # 根据规模 n 构造测试数据：
    # 简单策略：n 控制 n1、n2 的大小范围
    # n1 = n^2, n2 = 2*n^2 （保持差异且数值随 n 增长）
    n1 = n * n
    n2 = 2 * n * n

    ans = solve(n1, n2)
    fo(ans)


if __name__ == "__main__":
    # 示例：可自行修改 n 测试
    main(10)