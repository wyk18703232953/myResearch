def main(n):
    # n 作为查询数量 q
    q = n
    results = []
    for i in range(q):
        # 确定性生成区间 [l, r]
        l = 2 * i + 1
        r = l + (i % (n + 1))
        if l % 2 == 0:
            count = -((r - l + 1) // 2)

        else:
            count = ((r - l + 1) // 2)
        if (r - l + 1) % 2 == 0:
            results.append(count)

        else:
            if r % 2 == 0:
                results.append(count + r)

            else:
                results.append(count - r)
    for val in results:
        # print(val)
        pass
if __name__ == "__main__":
    main(10)