import random
import string


def solve_one(S: str, t: str) -> str:
    LENS = len(S)
    LENT = len(t)
    flag = 0

    for i in range(1, LENT + 1):
        t1 = t[:i]
        t2 = t[i:]

        DP = [-1] * (len(t1) + 1)
        DP[0] = 0

        for s in S:
            for j in range(len(t1), -1, -1):
                if 0 <= DP[j] < len(t2) and s == t2[DP[j]]:
                    DP[j] += 1

                if j > 0 and s == t1[j - 1]:
                    DP[j] = max(DP[j], DP[j - 1])

        if DP[-1] == len(t2):
            flag = 1
            break

    return "YES" if flag else "NO"


def generate_test_case(n: int):
    # 生成规模为 n 的测试数据：
    # 让 |S| 和 |t| 都与 n 同阶，这里简单设置为 |S| = n, |t| = n
    length_S = max(1, n)
    length_t = max(1, n)

    # 字符从小写字母中随机生成
    S = "".join(random.choice(string.ascii_lowercase) for _ in range(length_S))
    t = "".join(random.choice(string.ascii_lowercase) for _ in range(length_t))

    return S, t


def main(n: int):
    # 生成 n 组测试数据并运行
    results = []
    for _ in range(n):
        S, t = generate_test_case(n)
        res = solve_one(S, t)
        results.append(res)

    # 按原程序风格逐行输出
    for r in results:
        print(r)


if __name__ == "__main__":
    # 示例：运行 3 组规模为 3 的测试
    main(3)