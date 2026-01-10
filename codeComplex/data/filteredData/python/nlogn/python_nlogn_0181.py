def main(n):
    # 生成确定性区间数据：n 个 (x, w)
    # 这里令 x = i * 3, w = (i % 5) + 1
    rng = []
    for i in range(n):
        x = i * 3
        w = (i % 5) + 1
        rng.append((x - w, x + w))

    rng.sort(key=lambda x: (x[1], x[0]))

    ans = 0
    tmp = -10 ** 10
    for l, r in rng:
        if tmp <= l:
            ans += 1
            tmp = r

    print(ans)


if __name__ == "__main__":
    main(10)