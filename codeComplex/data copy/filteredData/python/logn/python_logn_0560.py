import sys
import math
import queue
import bisect

MOD = 998244353
sys.setrecursionlimit(1000000)


def solve(n: int) -> int:
    """
    原逻辑封装：返回对应的数字（int）
    """
    if n < 10:
        return n
    d = 1
    # 找到第 n 位所在的位数 d（1 位数、2 位数、3 位数...）
    while n > 9 * d * pow(10, d - 1):
        n -= 9 * d * pow(10, d - 1)
        d += 1
    # 此时 n 落在 d 位数区间内
    x = pow(10, d - 1) + (n - 1) // d   # 具体是哪个 d 位数
    p = n % d                            # 在该数的第几位（1-based）
    x = str(x).zfill(d)
    return int(x[p - 1])


def main(n: int):
    """
    n 为规模。这里示例：对从 1 到 n 的所有位置求值并输出最后一个结果。
    你可根据需要修改测试数据的生成方式。
    """
    # 根据规模 n 生成测试：这里简单用 n 本身作为原程序的参数，
    # 也可以生成多个测试，例如对 1..n 每个位置进行测试。
    # 为展示原逻辑，这里输出 solve(n) 的结果。
    ans = solve(n)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：将规模设为 100（可按需要修改）
    main(100)