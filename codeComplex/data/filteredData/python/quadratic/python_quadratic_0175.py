def main(n):
    # 解释规模含义：
    # n -> 数组 a 的长度
    # 生成方式完全确定：k 固定为 5，a[i] = (i * 7 + 3) % 256
    k = 5
    a = [(i * 7 + 3) % 256 for i in range(n)]

    p = [-1] * 256
    p[0] = 0

    for x in a:
        if p[x] < 0:
            for y in range(x - 1, max(-1, x - k), -1):
                if p[y] >= 0:
                    if p[y] + k > x:
                        p[x] = p[y]
                    else:
                        p[x] = p[y + 1] = y + 1
                    break
            if p[x] < 0:
                p[x] = p[x - k + 1] = x - k + 1

    b = [p[x] for x in a]
    print(' '.join(map(str, b)))


if __name__ == "__main__":
    main(10)