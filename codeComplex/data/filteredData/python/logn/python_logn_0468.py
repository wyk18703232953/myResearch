import random

def main(n: int):
    # 根据规模 n 生成两个非负整数 A、B
    # 使其位数不超过 30 位（与原程序循环 0..29 对应）
    max_val = min(n, (1 << 30) - 1)
    A = random.randint(0, max_val)
    B = random.randint(0, max_val)

    def ask(x, y, rev):
        # 原程序中 ask 返回 (A-B) 在某种交换/取反条件下的符号
        if rev == 0:
            return 1 if A - B > 0 else (-1 if A - B < 0 else 0)
        else:
            # 原代码中 rev==1 的时候返回 -input()，等价于对比较结果取反
            return - (1 if A - B > 0 else (-1 if A - B < 0 else 0))

    comp = ask(0, 0, 0)
    nowa = 0
    nowb = 0
    rev = 0

    for i in range(29, -1, -1):
        if comp < 0:
            rev ^= 1
            nowa, nowb = nowb, nowa
            comp = -comp
        if comp >= 0:
            comp = ask(nowa | (1 << i), nowb | (1 << i), rev)
            if comp < 0:
                nowa |= 1 << i
                comp = ask(nowa, nowb, rev)
            else:
                tmp = ask(nowa | (1 << i), nowb, rev)
                if tmp < 0:
                    nowa |= 1 << i
                    nowb |= 1 << i

    if rev == 1:
        nowa, nowb = nowb, nowa

    # 输出结果：还原出的 nowa, nowb，以及真实的 A, B 以便验证
    print("Recovered: ! %d %d" % (nowa, nowb))
    print("Actual   :   %d %d" % (A, B))


if __name__ == "__main__":
    # 示例运行，n 可根据需要调整
    main(10**9)