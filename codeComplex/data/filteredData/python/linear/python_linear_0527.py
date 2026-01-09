from collections import Counter

def main(n):
    # 映射：n -> (n, k=n)
    k = n
    # 构造长度为 n 的大写字母字符串，周期为 k 个字母（最多 26 个不同字母）
    # 但原程序中 k 是字母种类数，最大不能超过 26，否则访问 chr(ord('A')+i) 会超出大写字母范围
    # 为保持逻辑一致，这里将有效字母种类数设为 m = min(k, 26)
    m = min(k, 26)
    # 构造字符串：前 m 个位置使用 'A' 到 'A'+m-1，后续按同样周期重复
    s_chars = [chr(ord('A') + (i % m)) for i in range(n)]
    s = "".join(s_chars)

    c = Counter(s)
    ans = min(c[chr(ord('A') + i)] for i in range(m))
    result = m * ans
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)