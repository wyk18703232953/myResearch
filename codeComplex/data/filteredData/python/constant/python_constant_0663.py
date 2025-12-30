import random
import sys


def main(n: int):
    """
    n: 规模（比特数），将生成 0 <= a, b < 2^n 的随机数作为测试数据，
    并通过交互过程恢复出 a, b。
    """
    # 生成测试数据 a, b
    max_val = (1 << n) - 1
    a = random.randint(0, max_val)
    b = random.randint(0, max_val)

    # 为了可重复测试，可以打印到 stderr
    print(f"# hidden a={a}, b={b}, n={n}", file=sys.stderr)

    # 交互函数：比较 (a ^ c) 与 (b ^ d)
    def ask(c, d):
        # 若 (a ^ c) < (b ^ d) 返回 -1
        # 若 (a ^ c) == (b ^ d) 返回 0
        # 若 (a ^ c) > (b ^ d) 返回 1
        x = a ^ c
        y = b ^ d
        if x < y:
            return -1
        elif x > y:
            return 1
        else:
            return 0

    c = 0
    d = 0

    def solve(mi, base):
        nonlocal c, d

        def solve_same():
            nonlocal c, d
            print("# solve_same", file=sys.stderr)
            for i in range(mi, -1, -1):
                print(f">> {i=} {c=} {d=}", file=sys.stderr)
                bit = 1 << i
                res1 = ask(c ^ bit, d)
                res2 = ask(c, d ^ bit)
                if res1 == -1 and res2 == 1:
                    c |= bit
                    d |= bit

        def solve1():
            nonlocal c, d
            print("# solve1", file=sys.stderr)
            for i in range(mi, -1, -1):
                print(f">> {i=} {c=} {d=}", file=sys.stderr)
                bit = 1 << i
                res1 = ask(c ^ bit, d ^ bit)
                if res1 == -1:
                    # a[i] == 1, b[i] == 0
                    c |= bit
                    return solve(i - 1, ask(c, d))
                else:
                    # a[i] == b[i]
                    res2 = ask(c ^ bit, d)
                    if res2 == -1:
                        # a[i] == b[i] == 1
                        c |= bit
                        d |= bit

        def solve2():
            nonlocal c, d
            print("# solve2", file=sys.stderr)
            for i in range(mi, -1, -1):
                print(f">> {i=} {c=} {d=}", file=sys.stderr)
                bit = 1 << i
                res1 = ask(c ^ bit, d ^ bit)
                if res1 == 1:
                    # a[i] == 0, b[i] == 1
                    d |= bit
                    return solve(i - 1, ask(c, d))
                else:
                    # a[i] == b[i]
                    res2 = ask(c, d ^ bit)
                    if res2 == 1:
                        # a[i] == b[i] == 1
                        c |= bit
                        d |= bit

        if base == 0:
            solve_same()
        elif base == 1:
            solve1()
        else:
            solve2()

    # 从最高位 n-1 开始
    solve(n - 1, ask(0, 0))
    print("! {} {}".format(c, d))

    # 为验证算法正确性，可在 stderr 打印比较结果
    print(f"# recovered c={c}, d={d}", file=sys.stderr)
    print(f"# success={a == c and b == d}", file=sys.stderr)


if __name__ == "__main__":
    # 示例：n=30（与原程序 0..29 位一致）
    main(30)