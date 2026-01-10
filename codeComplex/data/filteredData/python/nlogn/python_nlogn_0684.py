def main(n):
    # 映射：n -> 列表长度
    m = n if n > 0 else 1

    # 确定性生成 a 和 s
    # a 为递增序列，元素适中
    a = [i % 7 + 1 for i in range(m)]
    # s 稍大一些保证多样性
    s = [i % 11 + 3 for i in range(m)]

    a = sorted(a)
    s = sorted(s)

    if a[-1] > s[0]:
        result = -1
    else:
        if a[-1] == s[0]:
            result = sum(a[:-1]) * m + sum(s)
        else:
            if m >= 2:
                result = sum(a[:-2]) * m + a[-2] * (m - 1) + sum(s) + a[-1]
            else:
                # m == 1 时，原逻辑中 a[:-2] 和 a[-2] 需要特别处理
                # sum(a[:-2]) 为 0，a[-2] 实际不存在，此时根据表达式合理退化
                # 表达式：sum(a[:-2])*m + a[-2]*(m-1) + sum(s) + a[-1]
                # 当 m==1 时，a[-2]*(m-1) 系数为 0，可忽略，只剩 sum(s) + a[-1]
                result = sum(s) + a[-1]

    print(result)


if __name__ == "__main__":
    main(10)