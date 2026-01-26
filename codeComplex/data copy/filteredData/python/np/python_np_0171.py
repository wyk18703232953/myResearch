def combine(n, k, w=1, out=None, result=None):
    if out is None:
        out = []
    if result is None:
        result = []
    if k == 0:
        result.append(out)
        return result
    for i in range(w, n + 1):
        new_out = out[:]
        new_out.append(i)
        combine(n, k - 1, i + 1, new_out, result)
    return result


def main(n):
    # 确定性生成输入数据
    # n: 原问题中的元素个数
    if n < 2:
        print(0)
        return

    # 生成 c: 长度为 n 的整数数组
    # c[i] = (i+1)*2，保证递增且简单
    c = [(i + 1) * 2 for i in range(n)]

    # 生成 l, r, x，使得区间可覆盖一定范围
    total_sum = sum(c)
    l = total_sum // 4 + 1
    r = (total_sum * 3) // 4 + 1
    x = max(1, (c[-1] - c[0]) // 3)

    result = None
    for i in range(2, n + 1):
        if i == n:
            result = combine(n, i)
        else:
            combine(n, i)

    for i in range(len(result)):
        comb = result[i]
        for j in range(len(comb)):
            comb[j] = c[comb[j] - 1]

    cnt = 0
    for i in range(len(result)):
        sm = sum(result[i])
        if sm >= l and sm <= r and (max(result[i]) - min(result[i]) >= x):
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main(5)