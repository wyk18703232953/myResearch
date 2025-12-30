import random

def ask(x, y, rev, A, B):
    # 比较函数：返回 (A^x) - (B^y)
    if rev == 1:
        x, y = y, x
    return (A ^ x) - (B ^ y)

def main(n):
    # 规模 n 用于生成 A, B 的随机范围，例如 [0, 2^n)
    if n <= 0 or n > 30:
        n = 30  # 限制位数，原程序循环到 2^29

    # 生成测试数据 A, B
    max_val = 1 << n
    A = random.randrange(max_val)
    B = random.randrange(max_val)

    comp = ask(0, 0, 0, A, B)
    nowa = 0
    nowb = 0
    rev = 0

    # 按照原代码，从高位到低位恢复 A, B
    for i in range(29, -1, -1):
        if comp < 0:
            rev ^= 1
            nowa, nowb = nowb, nowa
            comp = -comp
        if comp >= 0:
            comp = ask(nowa | (1 << i), nowb | (1 << i), rev, A, B)
            if comp < 0:
                nowa |= 1 << i
                comp = ask(nowa, nowb, rev, A, B)
            else:
                tmp = ask(nowa | (1 << i), nowb, rev, A, B)
                if tmp < 0:
                    nowa |= 1 << i
                    nowb |= 1 << i

    if rev == 1:
        nowa, nowb = nowb, nowa

    # 输出结果以及实际 A, B，以便检查
    print("Recovered A, B:", nowa, nowb)
    print("Actual    A, B:", A, B)
    return nowa, nowb, A, B

if __name__ == "__main__":
    # 示例：使用 10 位规模测试
    main(10)