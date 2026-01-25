def main(n):
    # n: length of sequence l and t
    n = int(n)
    if n <= 0:
        print(0)
        return

    # Deterministic generation of l (integers) and t (chars from 'GWL')
    # l[i] = 2 * ((i % 7) + 1)  -> positive even numbers, bounded pattern
    l = [2 * ((i % 7) + 1) for i in range(n)]
    pattern = "GWL"
    t_chars = [pattern[(i * 2 + 1) % 3] for i in range(n)]
    t = [pattern.index(ch) for ch in t_chars]

    mins = [0 for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        if t[i] != 2:
            mins[i] = max(mins[i + 1] - l[i], 0)
        else:
            mins[i] = mins[i + 1] + l[i]

    curs = ans = 0
    st = 0
    for i in range(n):
        if t[i] == 0:
            curs += l[i]
            ans += l[i] * 5
            if curs > mins[i + 1]:
                ol = (curs - mins[i + 1]) // 2
                if ol > l[i]:
                    ol = l[i]
                ans -= 4 * ol
                curs -= 2 * ol
        if t[i] == 1:
            st = 1
            curs += l[i]
            ans += l[i] * 3
        if t[i] == 2:
            if curs < l[i]:
                ol = l[i] - curs
                curs = l[i]
                ans += ol * (3 if st else 5)
            curs -= l[i]
            ans += l[i]
    if curs > 0:
        ans -= (curs // 2) * 2
    print(ans // 2)


if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(10)