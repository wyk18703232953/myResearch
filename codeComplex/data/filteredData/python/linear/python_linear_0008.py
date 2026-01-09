def main(n):
    # Generate n deterministic test strings mixing both formats
    # Pattern: for even i -> "R{row}C{col}", for odd i -> "{colLetters}{row}"
    # Scale row and column sizes with n for experimentation
    results = []
    for i in range(1, n + 1):
        row = i
        col = i * 7 + 3  # deterministic column number

        if i % 2 == 0:
            # RXCY format
            s = f"R{row}C{col}"

        else:
            # Column letters from col, then row number (e.g., BC23)
            c = col
            v = []
            while c > 0:
                if c % 26 == 0:
                    v.append('Z')
                    c = (c - 1) // 26

                else:
                    v.append(chr(ord('A') + (c % 26 - 1)))
                    c //= 26
            v.reverse()
            s = "".join(v) + str(row)

        # Apply original logic to s
        p = s.find('C')

        # R23C55 -> BC23
        if s[0] == 'R' and s[1].isdigit() and p > 1:
            r = int(s[1:p])
            c = int(s[(p + 1):])

            v = list()
            while c > 0:
                if c % 26 == 0:
                    v.append('Z')
                    c = (c - 1) // 26

                else:
                    v.append(chr(ord('A') + (c % 26 - 1)))
                    c //= 26

            v.reverse()
            results.append("%s%d" % ("".join(v), r))

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

            results.append("R%sC%d" % (sc, c))

    # Keep I/O minimal and deterministic: print all results
    for line in results:
        # print(line)
        pass
if __name__ == "__main__":
    main(10)