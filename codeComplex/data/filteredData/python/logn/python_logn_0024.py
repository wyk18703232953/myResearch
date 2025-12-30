import random

def main(n: int):
    # 1. 生成规模为 n 的测试数据：两个范围在 [0, 2^n - 1] 内的整数 l, r
    if n <= 0:
        return
    max_val = (1 << n) - 1
    l = random.randint(0, max_val)
    r = random.randint(0, max_val)

    # 2. 确保 l <= r（原程序使用 min/max 调整顺序）
    if l > r:
        l, r = r, l

    # 3. 以下为原算法逻辑的封装，无 input()，直接使用生成的 l, r
    r1 = len(bin(r)) - 3
    l1 = len(bin(l)) - 3
    ans = 0

    # 注意：如果 l == 0 原代码会跳过 while，保留 ans=0，然后走后续逻辑
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
    # 示例：调用 main(10) 生成规模为 10 的随机测试并执行
    main(10)