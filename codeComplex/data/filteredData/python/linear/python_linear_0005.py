def main(n):
    # Generate n deterministic test strings alternating both formats
    tests = []
    for i in range(1, n + 1):
        # Alternate between "R<row>C<col>" format and "EXCEL" format
        if i % 2 == 1:
            # R<row>C<col> form
            row = i
            col = i * 3
            tests.append(f"R{row}C{col}")

        else:
            # Column letters + row form
            row = i * 2
            col = i + 1
            # convert col to letters deterministically
            c = col
            v = ""
            while c:
                c -= 1
                r = c % 26
                c //= 26
                v += chr(65 + r)
            tests.append(f"{v[::-1]}{row}")

    for s in tests:
        ro = co = 0
        for c in s:
            if '0' <= c <= '9':
                ro = 10 * ro + int(c)
            elif ro:
                ro, co = s[1:].split('C')
                co = int(co)
                v = ''
                while co:
                    co -= 1
                    r = co % 26
                    co = co // 26
                    v += chr(65 + r)
                # print(v[::-1] + ro)
                pass
                break

            else:
                co = co * 26 + ord(c) - 64

        else:
            # print("R{}C{}".format(ro, co))
            pass
if __name__ == "__main__":
    main(10)