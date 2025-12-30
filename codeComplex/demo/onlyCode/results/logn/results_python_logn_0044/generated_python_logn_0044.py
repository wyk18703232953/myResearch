import random
import sys

INF = 10**9 + 7
sys.setrecursionlimit(INF)


def fo(*args):
    for s in args:
        sys.stdout.write(str(s) + ' ')
    sys.stdout.write('\n')


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
    # mask_arr[0] is the highest bit (2^63)
    for i in range(64):
        res = (res << 1) + mask_arr[i]
    return res


def main(n):
    """
    n: 规模参数，用于控制测试数据范围。
       将生成两个在 [0, 2^min(n, 60)) 范围内的随机整数 n1, n2。
    """
    # 根据 n 控制整数的位数，最多 60 位以避免溢出到 Python 超大整数范围之外
    bits = min(max(1, n), 60)
    upper = 1 << bits
    n1 = random.randrange(0, upper)
    n2 = random.randrange(0, upper)

    m1 = mask(n1)
    m2 = mask(n2)

    sol = [0 for _ in range(64)]

    # 找到第一位不同的比特并从该位开始置 1
    first_diff = 64  # 若完全相同则保持全 0
    for i in range(64):
        if m1[i] != m2[i]:
            sol[i] = 1
            first_diff = i
            break

    for j in range(first_diff + 1, 64):
        sol[j] = 1

    res = getn(sol)
    fo(res)


if __name__ == "__main__":
    # 示例调用：规模设为 10
    main(10)