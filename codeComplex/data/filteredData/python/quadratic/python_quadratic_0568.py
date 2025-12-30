import random

def main(n):
    # 随机生成 m，范围可按需调整，这里设为 [1, n]，至少为 1
    m = max(1, random.randint(1, n))

    np1 = n + 1
    mp1 = m + 1

    for i in range(1, 1 + n // 2):
        for j in range(1, mp1):
            print('%d %d\n%d %d' % (i, j, np1 - i, mp1 - j))

    if n & 1:
        i = 1 + n // 2
        for j in range(1, 1 + m // 2):
            print('%d %d\n%d %d' % (i, j, i, mp1 - j))

        if m & 1:
            print(i, 1 + m // 2)


if __name__ == "__main__":
    # 示例：可根据需要修改 n 的取值
    main(5)