def solution():
    n = int(input())
    for _ in range(n):
        s = input()
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
    solution()
