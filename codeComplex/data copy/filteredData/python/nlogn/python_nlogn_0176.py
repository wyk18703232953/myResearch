def main(n):
    # 生成确定性输入数据：n 个区间中心 x 和宽度 w
    # 映射：n 为区间数量
    li = []
    for i in range(n):
        x = i * 2
        w = (i % 5) + 1
        li.append((x - w, x + w))

    li.sort(key=lambda x: x[1])

    a = -10 ** 9
    ans = 0

    for i in range(n):
        if a <= li[i][0]:
            ans += 1
            a = li[i][1]

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)