import random

def main(n: int):
    # 生成测试数据：根据规模 n 生成 l, r（保证 0 <= l <= r）
    # 这里将数值规模控制在 [0, 2^n - 1] 内
    if n <= 0:
        l = 0
        r = 0
    else:
        max_val = (1 << n) - 1
        l = random.randint(0, max_val)
        r = random.randint(0, max_val)
        if l > r:
            l, r = r, l

    # 原始逻辑开始
    r1 = len(bin(r)) - 3
    l1 = len(bin(l)) - 3
    ans = 0

    while l > 0:
        if l1 == r1:
            r -= (1 << l1)
            l -= (1 << l1)
        else:
            ans = (1 << (r1 + 1)) - 1
            break

        z1 = min(l, r)
        z2 = max(l, r)
        l, r = z1, z2
        r1 = len(bin(r)) - 3
        l1 = len(bin(l)) - 3

    if ans == 0:
        if l1 == r1:
            if r == 1:
                print(1)
            else:
                print(0)
        else:
            print((1 << (r1 + 1)) - 1)
    else:
        print(ans)


if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数
    main(10)