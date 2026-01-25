def main(n):
    # Generate n deterministic test strings alternating between two formats.
    tests = []
    for i in range(1, n + 1):
        # Alternate between RC (e.g., "R23C55") and Excel-like (e.g., "BC23") formats
        if i % 2 == 1:
            # RC format
            r = i
            c = i * 3
            tests.append(f"R{r}C{c}")
        else:
            # Excel-like format
            # Generate a column name deterministically based on i
            col_num = i * 5
            v = []
            c = col_num
            while c > 0:
                if c % 26 == 0:
                    v.append('Z')
                    c = (c - 1) // 26
                else:
                    v.append(chr(ord('A') + (c % 26 - 1)))
                    c //= 26
            v.reverse()
            col_name = "".join(v)
            row = i * 2
            tests.append(f"{col_name}{row}")

    # Core algorithm logic from original solution
    for s in tests:
        p = s.find('C')

        # R23C55 -> BC23
        if s[0] == 'R' and len(s) > 1 and s[1].isdigit() and p > 1:
            r = int(s[1:p])
            c = int(s[(p + 1):])

            v = []
            while c > 0:
                if c % 26 == 0:
                    v.append('Z')
                    c = (c - 1) // 26
                else:
                    v.append(chr(ord('A') + (c % 26 - 1)))
                    c //= 26

            v.reverse()
            print("%s%d" % ("".join(v), r))

        else:
            p = 0
            while p < len(s):
                if s[p].isdigit():
                    break
                p += 1

            sr = s[:p]
            sc = s[p:]

            c = 0
            for x in sr:
                c = c * 26 + (ord(x) - ord('A') + 1)

            print("R%sC%d" % (sc, c))


if __name__ == "__main__":
    main(10)