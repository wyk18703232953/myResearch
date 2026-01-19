def main(n):
    # n 表示操作次数（原程序中的 m）
    m = n

    values = []
    idx = []
    outputs = []

    for i in range(m):
        # 确定性生成第 i 个输入 x
        x = (i * 17 + 23) ^ (i // 2)

        ans = 0
        for xx, ii in zip(values, idx):
            if (xx ^ x) < x:
                x ^= xx
                ans ^= ii
        if x == 0:
            anss = []
            tmp = ans
            for j in range(i):
                if (tmp & 1) != 0:
                    anss.append(j)
                tmp >>= 1
            outputs.append((len(anss), anss))
        else:
            outputs.append((0, []))
            values.append(x)
            idx.append(ans ^ (1 << i))

    # 将输出格式与原程序一致地打印出来
    for cnt, arr in outputs:
        if arr:
            print(cnt, *arr)
        else:
            print(0)


if __name__ == "__main__":
    main(10)