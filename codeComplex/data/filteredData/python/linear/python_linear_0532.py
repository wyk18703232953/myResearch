def main(n):
    # 映射：n -> 字符串长度，k 固定为 26（大写英文字母）
    k = 26
    count = [0] * k

    # 构造一个确定性的长度为 n 的字符串，使用周期性模式
    # 第 i 个字符为 chr(ord("A") + (i % k))
    s = ''.join(chr(ord("A") + (i % k)) for i in range(n))

    for c in s:
        count[ord(c) - ord("A")] += 1

    result = k * min(count)
    print(result)
    return result


if __name__ == "__main__":
    # 示例：使用 n = 100 作为规模
    main(100)