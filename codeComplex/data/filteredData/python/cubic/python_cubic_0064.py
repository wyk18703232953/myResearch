import random
import string


def main(n: int):
    # 1. 生成长度为 n 的随机小写字母串
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # 2. 原逻辑：统计重复出现过的子串中最长长度
    ans = 0
    m = set()
    for i in range(len(s)):
        for j in range(i, -1, -1):
            sub = s[j:i + 1]
            if sub in m:
                ans = max(ans, i - j + 1)
            else:
                m.add(sub)

    print(ans)


if __name__ == "__main__":
    # 示例：n = 10，可按需修改或在外部调用 main(n)
    main(10)