import random
import string

def main(n: int):
    # 1. 生成测试数据：长度为 n 的随机小写字符串 S
    # 为了尽量产生可重复子串，这里随机生成，但仍可能出现重复
    S = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    best = 0
    # 2. 原逻辑：寻找在 S 中至少出现 2 次的最长子串长度
    for i in range(len(S)):
        for j in range(i + 1, len(S) + 1):
            s = S[i:j]
            c = 0
            for k in range(len(S)):
                if S[k:].startswith(s):
                    c += 1
            if c >= 2:
                best = max(best, len(s))

    print(best)


if __name__ == "__main__":
    # 示例：调用 main，n 为测试数据规模
    main(20)