def main(n):
    # n 作为数组长度规模
    m = n
    k = max(1, n // 3)  # 保证 k >= 1
    # 构造一个确定性的递增序列，模拟原输入 p
    # 这里使用等差序列: p[i] = i*2 + 1
    p = [i * 2 + 1 for i in range(1, m + 1)]

    reduced = 1
    p.reverse()
    cnt = 0
    while len(p):
        cnt1 = 1
        first = p.pop()
        fack = ((first - reduced) // k) * k
        while len(p) and p[-1] - fack - reduced < k:
            cnt1 += 1
            p.pop()
        reduced += cnt1
        cnt += 1
    # print(cnt)
    pass
if __name__ == "__main__":
    main(10)