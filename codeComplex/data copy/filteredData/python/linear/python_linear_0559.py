def add(num):
    if num <= 1:
        return 0
    return (num * (num - 1)) // 2


def main(n):
    # 映射：n 为数组长度，k 为固定常数（可按需调整）
    if n <= 0:
        return

    k = 5  # 固定位数规模，保证算法逻辑不变

    # 确定性构造数组 a：利用简单算术和取模
    base_val = 2 ** k
    a = [(i * 17 + 23) % base_val for i in range(n)]

    pre = [a[0]]
    base = (2 ** k) - 1
    hb = 2 ** (k - 1)

    for i in range(1, n):
        pre.append(a[i] ^ pre[-1])

    cnt = {}
    cnt[0] = [0, 0]

    for i in range(n):
        if pre[i] >= hb:
            key = base - pre[i]
            if key not in cnt:
                cnt[key] = [0, 0]
            cnt[key][1] += 1

        else:
            key = pre[i]
            if key not in cnt:
                cnt[key] = [0, 0]
            cnt[key][0] += 1

    cnt1 = 0
    for v in cnt.values():
        sum1 = v[0] + v[1]
        cnt1 += add(sum1 // 2)
        cnt1 += add((sum1 + 1) // 2)
    cnt1 += sum(cnt[0]) // 2

    result = (n * (n + 1)) // 2 - cnt1
    # print(result)
    pass
if __name__ == "__main__":
    main(10)