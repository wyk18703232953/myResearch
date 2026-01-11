def main(n):
    # Generate deterministic input of size n:
    # Build a string similar to original input(): tokens like "1m", "2p", "3s"
    # We cycle digits 1..9 and suits 'm','p','s' based on index.
    suits = 'mps'
    tokens = []
    for i in range(n):
        digit = (i % 9) + 1  # 1..9
        suit = suits[(i // 9) % 3]  # cycle through m, p, s in blocks of 9
        tokens.append(str(digit) + suit)
    input_str = " ".join(tokens)

    f = lambda c: 'mps'.index(c)
    l = [[], [], []]
    for c in input_str.split():
        a, b = c
        l[f(b)].append(int(a))
    for i in range(3):
        l[i].sort()

    res = 3
    for x in l:
        if len(x) == 0:
            continue
        elif len(x) == 1:
            res = min(res, 2)
        elif len(x) == 3:
            if len(set(x)) == 1:
                res = min(res, 0)
                break
            if x[0] == x[1] - 1 and x[1] == x[2] - 1:
                res = min(res, 0)
                break
        res = min(res, 2)
        for i in range(len(x)):
            for j in range(i + 1, len(x)):
                if abs(x[i] - x[j]) <= 2:
                    res = min(res, 1)
    # print(res)
    pass
if __name__ == "__main__":
    main(9)