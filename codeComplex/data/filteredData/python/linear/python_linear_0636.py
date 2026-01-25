def main(n):
    lst = []
    lst.append(0)
    lst.append(1)

    now = 1
    # build lst exactly as original code does
    while now <= 1e25:
        now = now * 4 + 1
        lst.append(now)

    # deterministic generation of t test cases from n
    t = max(1, n)
    print(t)

    for i in range(t):
        # generate n_i and k_i deterministically from i and n
        ni = max(1, (i % 40) + (n % 5))
        ki = (i + 1) * (n + 1)

        print(ni, ki)

        if ni >= 34:
            print("YES " + str(ni - 1))
            continue

        sek = 0
        ambil = 1
        nyak = 0
        cnt = 0
        sudah = False

        while sek < ni:
            cnt = cnt + (1 << (sek + 1)) - 1
            if cnt > ki:
                print("NO")
                sudah = True
                break

            next_ambil = (ambil + 1) * 2 - 1
            sisa = 4 * ambil - next_ambil
            ambil = next_ambil

            sek += 1
            nyak = nyak + sisa * lst[ni - sek]
            if (nyak + cnt) >= ki:
                print("YES " + str(ni - sek))
                sudah = True
                break

        if not sudah:
            print("NO")


if __name__ == "__main__":
    main(10)