def main(n: int):
    # 生成测试数据：
    # 构造一个长度为 tam 的字符串 t 和重复次数 q
    # 为了可控，这里令：
    #   tam = n
    #   q = n
    #   t = 由 'a' 开头，接着 (tam-1) 个循环字母（a-z）构成
    if n <= 0:
        return ""

    tam = n
    q = n
    # 构造字符串 t，长度为 tam
    base_chars = [chr(ord('a') + (i % 26)) for i in range(tam)]
    t = "".join(base_chars)

    s = t
    posi = -1

    # 寻找最长前缀，使其等于后缀
    for j in range(tam - 1):
        if t[: j + 1] == t[tam - j - 1 :]:
            posi = j

    add = t[posi + 1 :]

    for _ in range(q - 1):
        s += add

    print(s)
    return s


if __name__ == "__main__":
    # 示例运行：可根据需要修改 n
    main(5)