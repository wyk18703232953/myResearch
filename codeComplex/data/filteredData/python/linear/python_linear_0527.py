from collections import Counter
import random
import string


def main(n):
    # 随机生成 k (1 <= k <= 26, 且 k <= n)
    k = random.randint(1, min(26, n)) if n > 0 else 1

    # 从前 k 个大写字母中生成长度为 n 的字符串
    alphabet = string.ascii_uppercase[:k]
    s = ''.join(random.choice(alphabet) for _ in range(n))

    # 原逻辑
    c = Counter(s)
    ans = min(c[chr(ord('A') + i)] for i in range(k))
    print(k * ans)


if __name__ == "__main__":
    # 示例：可根据需要修改 n
    main(10)