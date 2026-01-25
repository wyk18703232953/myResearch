def main(n):
    # 生成确定性的 first 和 last，长度由 n 决定
    # 保证 n >= 1 时不过短，限制最大长度以防极端情况
    length = max(1, min(n, 1000))
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # 构造 first：循环使用字母表
    first = "".join(alphabet[i % 26] for i in range(length))

    # 构造 last：与 first 有一定差异但确定性
    last = "".join(alphabet[(i * 3 + 5) % 26] for i in range(length))

    # 保持原始算法逻辑
    username = first[0]
    first_rest = first[1:]
    while first_rest != "" and first_rest[0] < last[0]:
        username = username + first_rest[0]
        first_rest = first_rest[1:]
    result = username + last[0]

    print(result)


if __name__ == "__main__":
    main(10)