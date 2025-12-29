import random
import string


def main(n: int):
    # 生成测试数据：
    # s1 为长度 n 的随机小写字符串
    # s2 为长度至少 1 的随机小写字符串，这里固定长度为 n（最少保证1）
    n = max(1, n)
    s1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))
    s2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(max(1, n)))

    # 原逻辑开始
    res = s1[0]
    flag = 0
    for i in range(1, len(s1)):
        if s1[i] >= s2[0]:
            res += s2[0]
            flag = 1
            break
        else:
            res += s1[i]
    if flag == 0:
        res += s2[0]

    print(res)


if __name__ == "__main__":
    # 可根据需要修改默认 n
    main(5)