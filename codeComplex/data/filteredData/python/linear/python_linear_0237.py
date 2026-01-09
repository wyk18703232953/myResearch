def main(n):
    ALPHABET = [chr(i) for i in range(65, 65+26)] + [chr(i) for i in range(97, 97+26)]

    def generate_string(length):
        chars = []
        for i in range(length):
            chars.append(ALPHABET[i % len(ALPHABET)])
        return chars

    # Interpret n as the length of each string
    L = max(1, n)

    black = generate_string(L)
    white = generate_string(L + 1 if L > 1 else 1)
    katie = generate_string(L + 2 if L > 2 else L)

    def optimal_score(LIST):
        d = {char: 0 for char in ALPHABET}
        for v in LIST:
            d[v] += 1
        max_freq = max(d.values())
        Llen = len(LIST)
        res = 0
        for freq in d.values():
            if Llen - freq >= n:
                res = max(res, freq + n)

            else:
                if not (Llen - freq < n and n == 1):
                    res = Llen

                else:
                    res = max(res, Llen - 1)
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