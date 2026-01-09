from collections import Counter

def main(n):
    # 映射规则：
    # k 为字母种类数，限定在 [1, 26]
    # n 为字符串长度
    k = (n % 26) + 1  # 保证 1 <= k <= 26
    # 生成确定性字符串，使用循环字母序列
    base_chars = [chr(ord('A') + (i % k)) for i in range(n)]
    s = ''.join(base_chars)

    c = Counter(s)
    min_symbols = min(c[chr(ord("A") + i)] for i in range(k))
    result = min_symbols * k
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)