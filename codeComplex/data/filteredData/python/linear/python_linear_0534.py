from collections import Counter


def main(n):
    # 映射：k = n，字符串长度也取为 n
    k = max(1, n)
    length = k

    # 构造确定性字符串：周期性使用从 'A' 到 'A'+k-1 的字符
    alphabet = [chr(ord("A") + i) for i in range(k)]
    s = "".join(alphabet[i % k] for i in range(length))

    c = Counter(s)
    min_symbols = min(c[chr(ord("A") + i)] for i in range(k))
    # print(min_symbols * k)
    pass
if __name__ == "__main__":
    main(10)