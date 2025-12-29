import random
import string


def main(n: int) -> None:
    # 1. 生成长度为 n 的测试字符串，使用小写字母
    # 如需固定随机性，可在外部设置 random.seed()
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # 2. 保持原逻辑：统计所有子串出现次数，找出现至少 2 次的最长子串长度
    d = {}
    for i in range(n):
        r = ""
        for j in range(i, n):
            r += s[j]
            if r not in d:
                d[r] = 1
            else:
                d[r] += 1

    maxi = 0
    for sub, cnt in d.items():
        if cnt >= 2:
            maxi = max(maxi, len(sub))

    print(maxi)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)