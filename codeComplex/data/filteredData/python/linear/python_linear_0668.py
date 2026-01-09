def main(n):
    # Interpret n as the length of the lists l and t
    # Deterministic generation of l and t
    # l: positive integers scaled deterministically
    l = [(i % 7 + 1) * 2 for i in range(n)]
    # t: cycle through 'G', 'W', 'L' encoded via "GWL".index
    t = [i % 3 for i in range(n)]  # 0->G,1->W,2->L

    mins = [0 for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        if t[i] != 2:
            mins[i] = max(mins[i + 1] - l[i], 0)

        else:
            mins[i] = mins[i + 1] + l[i]

    curs = ans = st = 0
    for i in range(n):
        if t[i] == 0:
            curs += l[i]
            ans += l[i] * 5
            if curs > mins[i + 1]:
                ol = (curs - mins[i + 1]) // 2
                ol = min(ol, l[i])
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
        ans -= curs // 2 * 2
    # print(ans // 2)
    pass
if __name__ == "__main__":
    # Example call for time-complexity experiments
    main(10_000)