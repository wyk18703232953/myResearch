import random

def main(n: int):
    # 随机生成满足原代码逻辑的 a, b 测试数据
    # 需避免直接导致 "NO" 的组合：min(a,b) > 1 或 (1 < n < 4 and max(a,b) == 1)
    if n <= 1:
        # n=1 时随便选，保证可构造
        a, b = 1, 1
    else:
        while True:
            # 按原题大致范围随机，可按需调整
            a = random.randint(1, n)
            b = random.randint(1, n)
            if not (min(a, b) > 1 or (1 < n < 4 and max(a, b) == 1)):
                break

    # 以下为原逻辑，只是从 input 改为用生成的 a, b
    if min(a, b) > 1 or 1 < n < 4 and max(a, b) == 1:
        print('NO')
        return

    print('YES')
    f = int(a == 1)
    g = [a, b][f]
    r = [[f] * n for _ in range(n)]
    for i in range(n):
        r[i][i] = 0
    for i in range(n - g):
        r[i][i + 1] ^= 1
        r[i + 1][i] ^= 1
    for x in r:
        print(*x, sep='')


if __name__ == "__main__":
    # 调试时可在这里指定 n
    main(5)