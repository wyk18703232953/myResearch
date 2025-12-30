import random
import string

def main(n: int):
    # 生成测试数据：长度为 n 的随机小写字母串
    # 为了保证多样性，随机从 1~min(26, n) 中选取不同字符数量
    distinct_chars = random.randint(1, min(26, max(1, n)))
    chars = random.sample(string.ascii_lowercase, distinct_chars)
    s = ''.join(random.choice(chars) for _ in range(n))

    # 原算法逻辑
    want = len(set(s))  # 字符串中不同字符的数量
    d = {}
    j = 0
    count = 0
    ans = float("inf")

    for i in range(n):
        if s[i] not in d:
            d[s[i]] = 0
            count += 1
        d[s[i]] += 1
        if count == want:
            while d[s[j]] > 1:
                d[s[j]] -= 1
                j += 1
            ans = min(ans, i - j + 1)

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(20)
    main(20)