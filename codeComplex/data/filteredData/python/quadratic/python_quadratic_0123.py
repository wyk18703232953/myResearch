import random

mod = 10**9 + 7
INF = float('inf')


def main(n):
    # 随机生成 m（边数/元素数），这里设为 1~2n 之间
    m = random.randint(1, 2 * n)

    # 生成长度为 m 的数组 c，元素在 1..n 之间，仿照原题的 1-based 输入
    c = [random.randint(1, n) for _ in range(m)]

    # 原程序逻辑开始
    cnt = [0] * n
    # 原程序将输入减 1 转为 0-based，这里直接在生成时减 1
    for x in c:
        cnt[x - 1] += 1

    # 输出答案
    print(min(cnt))


if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时由外部决定 n
    main(5)