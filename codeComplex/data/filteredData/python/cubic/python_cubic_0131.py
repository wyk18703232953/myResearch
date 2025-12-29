import random
import string


def problem(s, p):
    for i in range(len(p)):
        l = p[:i] + ' '
        r = p[i:] + ' '

        dp = [0] + [None] * i

        for x in s:
            for j in range(i, -1, -1):
                if dp[j] is None:
                    continue

                if l[j] == x:
                    dp[j + 1] = dp[j] if dp[j + 1] is None else max(dp[j], dp[j + 1])

                if r[dp[j]] == x:
                    dp[j] += 1

        if dp[-1] == len(r) - 1:
            return 'YES'

    return 'NO'


def main(n):
    # 生成 n 组测试数据
    # 这里将字符串长度控制在 1~n，字符来自小写字母
    random.seed(0)
    for _ in range(n):
        len_s = random.randint(1, n)
        len_p = random.randint(1, n)
        s = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_s))
        p = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_p))
        print(problem(s, p))


if __name__ == "__main__":
    # 示例：运行 5 组随机测试
    main(5)