def main(n):
    # 映射：n -> (n, m) 其中 m = n
    m = n
    # 确定性构造数组 a，长度为 m
    # 示例构造：a[i] = (i * 2 + 3) % (n + 5) + 1，保证为正整数且有一定分布
    a = [((i * 2 + 3) % (n + 5)) + 1 for i in range(m)]
    a.sort()

    ans = 0
    cur = 0
    for b in a:
        if b > cur:
            ans += 1
            cur += 1

        else:
            ans += 1
    result = sum(a) - (ans + max(a) - cur)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)