def main(n):
    # Interpret n as the length of each input string
    if n <= 0:
        return

    ALPHABET = [chr(i) for i in range(65, 65 + 26)] + [chr(i) for i in range(97, 97 + 26)]

    # Deterministically generate three strings of length n over ALPHABET
    black = [ALPHABET[i % len(ALPHABET)] for i in range(n)]
    white = [ALPHABET[(i * 2) % len(ALPHABET)] for i in range(n)]
    katie = [ALPHABET[(i * 3) % len(ALPHABET)] for i in range(n)]

    def optimal_score(LIST):
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

    score_black = optimal_score(black)
    score_white = optimal_score(white)
    score_katie = optimal_score(katie)

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
        # print(winner)
        pass

    else:
        # print("Draw")
        pass
if __name__ == "__main__":
    main(10)