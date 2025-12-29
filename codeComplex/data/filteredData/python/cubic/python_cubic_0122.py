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
    # 根据规模 n 生成 n 组测试数据
    random.seed(0)
    results = []
    for _ in range(n):
        # 随机生成 s 和 p，长度相对较小，便于测试
        len_s = random.randint(1, 10)
        len_p = random.randint(1, 10)
        s = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_s))
        p = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_p))
        results.append(problem(s, p))
    # 输出结果
    for res in results:
        print(res)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)