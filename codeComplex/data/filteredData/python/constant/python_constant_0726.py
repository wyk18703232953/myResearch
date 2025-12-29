def main(n):
    import sys
    import random

    # 根据 n 生成测试数据 k，范围保持和原程序一致：1 ~ 10^12
    # 这里将上界设为 min(10^12, n)，确保可根据 n 调整规模
    upper = min(10**12, max(1, n))
    k = random.randint(1, upper)

    # 原逻辑开始
    if not isinstance(k, int) or k <= 0 or k > 10**12:
        print("wrong input. try again")
        sys.exit()

    lim_init = lim = decimal = 9
    c = 0
    while True:
        c += 1
        if k <= lim:
            diff = lim - k
            pos = diff % c
            diff = int(diff / c)
            diff = decimal - diff
            print(''.join(list(reversed(str(diff))))[pos])
            break
        else:
            decimal = int(str(lim_init) * (c + 1))
            lim += int(str(lim_init) + '0' * c) * (c + 1)


if __name__ == "__main__":
    # 示例：将规模参数设置为 10^6，可按需修改
    main(10**6)