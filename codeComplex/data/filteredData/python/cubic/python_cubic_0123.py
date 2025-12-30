from sys import stdout
import random
import string

nxt = []


def find_it(s, left, right):
    global nxt
    dp = [[1000 for _ in range(len(right) + 1)] for _ in range(len(left) + 1)]
    dp[0][0] = 0
    for i in range(len(left) + 1):
        for j in range(len(right) + 1):
            if dp[i][j] > len(s):
                continue
            if j < len(right) and nxt[ord(right[j]) - 97][dp[i][j]] != -1:
                if nxt[ord(right[j]) - 97][dp[i][j]] < dp[i][j + 1]:
                    dp[i][j + 1] = nxt[ord(right[j]) - 97][dp[i][j]] + 1
            if i < len(left) and nxt[ord(left[i]) - 97][dp[i][j]] != -1:
                if nxt[ord(left[i]) - 97][dp[i][j]] < dp[i + 1][j]:
                    dp[i + 1][j] = nxt[ord(left[i]) - 97][dp[i][j]] + 1
    return dp[len(left)][len(right)] != 1000


def solve_case(s, t):
    global nxt
    nxt = [[-1 for _ in range(len(s) + 1)] for _ in range(26)]
    for i, x in enumerate(s):
        nxt[ord(x) - 97][i] = i
    for i in range(26):
        for j in range(len(s) - 1, -1, -1):
            if nxt[i][j] != j:
                nxt[i][j] = nxt[i][j + 1]

    for i in range(len(t)):
        if find_it(s, t[:i], t[-len(t) + i:]):
            return True
    return False


def main(n):
    # 生成 n 组测试数据并输出结果
    # 规模 n 控制测试用例数量；字符串长度根据 n 简单设置，可自行调整
    random.seed(1)
    for _ in range(n):
        len_s = max(1, n % 20 + 5)
        len_t = max(1, (n * 2) % 20 + 5)
        s = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_s))
        t = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_t))

        if solve_case(s, t):
            stdout.write("YES\n")
        else:
            stdout.write("NO\n")


if __name__ == "__main__":
    # 示例：运行 3 组随机测试
    main(3)