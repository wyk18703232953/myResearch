import random

def main(n: int):
    # 1. 生成规模为 n 的测试数据
    # 这里生成 n 个范围在 [-10^9, 10^9] 的随机整数
    s = [random.randint(-10**9, 10**9) for _ in range(n)]

    # 2. 原始逻辑
    d = {}
    for x in s:
        d[x] = d.get(x, 0) + 1

    rem = 0
    for i in range(n):
        ok = False
        for j in range(31):
            x = (1 << j) - s[i]  # 2**j - s[i]
            c = d.get(x, 0)
            if c > 1 or (c == 1 and s[i] != x):
                ok = True
                break
        if not ok:
            rem += 1

    print(rem)


if __name__ == "__main__":
    # 可在此处修改 n 进行本地测试
    main(10)