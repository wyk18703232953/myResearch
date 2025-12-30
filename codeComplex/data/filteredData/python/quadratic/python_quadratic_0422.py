import random
import string

def main(n: int):
    # 随机生成 n 和 k（k 至少为 1，适当限制上界）
    if n <= 0:
        return

    k = random.randint(1, 10)

    # 随机生成长度为 n 的字符串 s（小写字母）
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    ap = 0
    i = 1
    while i < n:
        if s[:i] == s[-i:]:
            ap = i
        i += 1

    result = s + s[ap:] * (k - 1)
    print(result)


if __name__ == "__main__":
    # 示例运行：可以根据需要修改 n 的默认测试规模
    main(5)