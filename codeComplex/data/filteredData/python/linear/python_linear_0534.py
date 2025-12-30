from collections import Counter
import random
import string


def main(n):
    # 生成规模为 n 的测试数据
    # 约束：1 <= k <= 26，且 k <= n（否则无法构造长度为 n 的字符串覆盖前 k 个字母）
    k = min(26, max(1, n // 2))  # 示例策略：k 不超过 26，且随 n 变化
    # 使用大写字母 A-Z 中的前 k 个作为可选字符
    letters = string.ascii_uppercase[:k]

    # 为了避免某个字母计数为 0，这里先保证每个字母至少出现一次
    s_list = list(letters)
    # 剩余位置随机填充
    if n > k:
        s_list += [random.choice(letters) for _ in range(n - k)]
    random.shuffle(s_list)
    s = "".join(s_list)

    # 原始逻辑
    c = Counter(s)
    min_symbols = min(c[chr(ord("A") + i)] for i in range(k))
    result = min_symbols * k

    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改或在外部调用 main
    main(10)