def main(n):
    # Generate n test cases, each with 3 "cards" like '1m', '2p', etc.
    # Card numbers: 1..9 (wrap via i % 9 + 1)
    # Suits: 'm', 'p', 's'
    suits = ['m', 'p', 's']
    results = []

    for i in range(n):
        # Deterministic generation of 3 cards per test case
        c1 = str((3 * i) % 9 + 1) + suits[(3 * i) % 3]
        c2 = str((3 * i + 1) % 9 + 1) + suits[(3 * i + 1) % 3]
        c3 = str((3 * i + 2) % 9 + 1) + suits[(3 * i + 2) % 3]
        t = [c1, c2, c3]

        # Original core logic
        t.sort()

        if t.count(t[0]) == 3:
            res = '0'
        elif t.count(t[0]) == 2 or t.count(t[1]) == 2:
            res = '1'
        else:
            num = list(map(int, [t[0][0], t[1][0], t[2][0]]))
            suit = [t[0][1], t[1][1], t[2][1]]
            if len(set(suit)) == 3:
                res = '2'
            elif len(set(suit)) == 1:
                if num[1] == num[0] + 1 or num[2] == num[1] + 1:
                    if num[2] == num[0] + 2:
                        res = '0'
                    else:
                        res = '1'
                elif num[1] == num[0] + 2 or num[2] == num[1] + 2:
                    res = '1'
                else:
                    res = '2'
            else:
                if suit[0] == suit[1]:
                    if num[1] - num[0] in [1, 2]:
                        res = '1'
                    else:
                        res = '2'
                elif suit[1] == suit[2]:
                    if num[2] - num[1] in [1, 2]:
                        res = '1'
                    else:
                        res = '2'
                else:
                    if num[2] - num[0] in [1, 2]:
                        res = '1'
                    else:
                        res = '2'
        results.append(res)

    # Aggregate output so the work scales with n but I/O stays small
    print("\n".join(results))


if __name__ == "__main__":
    main(10)