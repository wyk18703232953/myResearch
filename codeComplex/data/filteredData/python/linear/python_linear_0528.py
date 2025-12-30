import random
import string

def main(n):
    # 1 <= k <= min(26, n)
    k = random.randint(1, min(26, n))

    # 生成由大写字母 A-Z 组成的长度为 n 的字符串
    # 为了更有意义，优先在前 k 个字母中采样
    letters = string.ascii_uppercase[:k]
    # 若 n > k，允许重复采样；若要保证覆盖可以再加逻辑
    s = ''.join(random.choice(letters) for _ in range(n))

    # 原逻辑
    c = [0] * 26
    for i in range(n):
        if s[i] <= chr(ord('A') + k - 1):
            c[ord(s[i]) - ord('A')] += 1
    print(min(c[:k]) * k)

if __name__ == "__main__":
    # 示例：规模 n = 20
    main(20)