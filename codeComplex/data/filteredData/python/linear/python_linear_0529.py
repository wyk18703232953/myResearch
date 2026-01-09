def main(n):
    # 映射：n -> k, 字符串长度 = n, 使用前 k 个大写字母周期构造字符串
    k = max(1, min(26, n if isinstance(n, int) and n > 0 else 1))
    length = n if isinstance(n, int) and n > 0 else k

    # 构造确定性字符串 s：按前 k 个大写字母循环
    s = ''.join(chr(ord('A') + (i % k)) for i in range(length))

    m = 10 ** 10
    for i in range(k):
        c = chr(ord('A') + i)
        m = min(m, s.count(c))
    result = m * k
    return result


if __name__ == "__main__":
    # print(main(10))
    pass