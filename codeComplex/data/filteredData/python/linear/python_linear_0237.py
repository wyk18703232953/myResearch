import random
import string

ALPHABET = [chr(i) for i in range(65, 65 + 26)] + [chr(i) for i in range(97, 97 + 26)]


def optimal_score(LIST, n):
    d = {char: 0 for char in ALPHABET}
    for v in LIST:
        d[v] += 1
    max_freq = max(d.values())
    L = len(LIST)
    res = 0
    for freq in d.values():
        if L - freq >= n:
            res = max(res, freq + n)
        else:
            if not (L - freq < n and n == 1):
                res = L
            else:
                res = max(res, L - 1)
    return res


def main(n: int):
    # 根据 n 生成测试数据：三个长度为 n 的随机字符串
    chars = ALPHABET
    black = [random.choice(chars) for _ in range(n)]
    white = [random.choice(chars) for _ in range(n)]
    katie = [random.choice(chars) for _ in range(n)]

    score_black = optimal_score(black, n)
    score_white = optimal_score(white, n)
    score_katie = optimal_score(katie, n)

    M = max(score_black, score_katie, score_white)
    MAXCNT = 0

    winner = "NOBODY"

    if M == score_black:
        winner = "Kuro"
        MAXCNT += 1
    if M == score_white:
        winner = "Shiro"
        MAXCNT += 1
    if M == score_katie:
        winner = "Katie"
        MAXCNT += 1

    if MAXCNT == 1:
        print(winner)
    else:
        print("Draw")


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)