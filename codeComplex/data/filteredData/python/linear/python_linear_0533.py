from collections import Counter
import random
import string

def main(n):
    # 这里的 n 用作字符串长度规模
    # 随机生成 k (1 <= k <= 26)
    k = random.randint(1, 26)

    # 从前 k 个大写字母中随机生成长度为 n 的字符串 s
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    valid_chars = alpha[:k]
    s = ''.join(random.choice(valid_chars) for _ in range(n))

    # 原始逻辑
    c = Counter(s)
    mn = 10 ** 9
    for ch in valid_chars:
        mn = min(mn, c[ch])
    result = mn * k

    # 按需返回或打印结果，这里选择打印
    print(result)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可在此修改
    main(10)