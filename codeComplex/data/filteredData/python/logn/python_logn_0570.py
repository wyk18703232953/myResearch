from math import log10
from random import randint

aa = [9, 99, 999, 9999, 99999, 999999, 9999999, 99999999, 999999999, 9999999999]
a = [9, 189, 2889, 38889, 488889, 5888889, 68888889, 788888889, 8888888889,
     98888888889, 1088888888889]


def solve_one(n: int) -> int:
    if n in a:
        n = 9
    if n < 10:
        return n
    x = 1
    while a[x] < n:
        x += 1
    v = n - a[x - 1]
    z = v // (x + 1)
    z += aa[x - 1]
    v %= (x + 1)
    if not v:
        p = z % 10
    else:
        z += 1
        p = int(str(z)[v - 1])
    return p


def main(n: int):
    """
    n 作为规模参数，用来控制生成的测试数据范围。
    这里约定：
      - 生成一个随机整数 q，范围在 [1, min(max_a, n)] 内，
        其中 max_a 是预处理数组 a 中的最大可处理位置。
      - 然后对该 q 运行原逻辑并输出结果。

    你也可以根据需要把 q 的生成方式改成线性、均匀遍历等。
    """
    max_a = a[-1]  # 1088888888889
    upper = min(max_a, max(1, n))
    q = randint(1, upper)  # 生成测试数据

    ans = solve_one(q)
    print(ans)


if __name__ == "__main__":
    # 示例：用一个固定规模调用 main，可按需修改或删除
    main(10**6)