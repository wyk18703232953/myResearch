def main(n):
    # Generate deterministic input: n "cards" each like "1m", "2s", "3p" cyclically
    # Original logic expects at most 3, but we scale by using first 3 occurrences per suit
    suits = ['m', 's', 'p']
    ls = []
    for i in range(n):
        value = (i % 9) + 1  # values 1..9 cyclic
        suit = suits[i % 3]
        ls.append(str(value) + suit)

    d = {'m': [], 's': [], 'p': []}
    for token in ls:
        d[token[1]].append(int(token[0]))

    for k, v in d.items():
        v.sort()
        if len(v) == 3 and len(set(v)) == 1:
            print(0)
            break
        if len(v) == 3 and v[0] + 1 == v[1] and v[1] + 1 == v[2]:
            print(0)
            break
    else:
        for k, v in d.items():
            if len(v) == 2 and len(set(v)) == 1:
                print(1)
                break
            if len(v) == 2 and v[1] - v[0] <= 2:
                print(1)
                break
            if len(v) == 3 and (v[0] == v[1] or v[1] == v[2]):
                print(1)
                break
            if len(v) == 3 and (v[1] - v[0] <= 2 or v[2] - v[1] <= 2):
                print(1)
                break
        else:
            print(2)


if __name__ == "__main__":
    main(9)