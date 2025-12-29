import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里假设 n 为 a,b 的最大可能值
    if n <= 1:
        n = 2
    a = random.randint(0, n)
    b = random.randint(0, n)

    # 原逻辑开始
    a, b = min(a, b), max(a, b)

    bina = bin(a)[2:]
    binb = bin(b)[2:]

    lena = len(bina)
    lenb = len(binb)

    ans = 0
    if lena != lenb:
        ans = 2 ** lenb - 1
    else:
        # 原代码此处有 bug：应对 binb 补零，而不是对 a
        bina = bina.zfill(lenb)
        for i in range(lenb):
            if (bool(int(bina[i])) != bool(int(binb[i]))):
                ans = 2 ** (lenb - i) - 1
                break

    print(ans)


if __name__ == "__main__":
    # 示例：以 100 为规模调用
    main(100)