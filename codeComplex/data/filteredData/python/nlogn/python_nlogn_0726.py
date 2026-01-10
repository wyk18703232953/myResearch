def main(n):
    results = []
    # Generate n deterministic test cases of three 2-character strings each.
    # Characters are digits '1'..'9' and suits 'a','b','c'
    for i in range(n):
        d1 = str((i % 9) + 1)
        d2 = str(((i // 3) % 9) + 1)
        d3 = str(((i // 7) % 9) + 1)
        s1 = chr(ord('a') + (i % 3))
        s2 = chr(ord('a') + ((i // 2) % 3))
        s3 = chr(ord('a') + ((i // 4) % 3))
        a = d1 + s1
        b = d2 + s2
        c = d3 + s3

        if a == b and b == c:
            results.append("0")
        elif a == b or b == c or a == c:
            results.append("1")
        else:
            na = int(a[0])
            nb = int(b[0])
            nc = int(c[0])
            if a[1] == b[1] and a[1] == c[1]:
                cp = [na, nb, nc]
                cp.sort()
                cp[0] += 2
                cp[1] += 1
                if cp[0] == cp[1] and cp[1] == cp[2]:
                    results.append("0")
                elif (
                    cp[0] == cp[1]
                    or cp[1] == cp[2]
                    or cp[0] == cp[1]
                    or (cp[0] + 1) == cp[1]
                    or (cp[1] + 1) == cp[2]
                ):
                    results.append("1")
                else:
                    results.append("2")
            elif a[1] == b[1]:
                mi = min(na, nb)
                ma = max(na, nb)
                if mi == (ma - 1) or mi == (ma - 2):
                    results.append("1")
                else:
                    results.append("2")
            elif a[1] == c[1]:
                mi = min(na, nc)
                ma = max(na, nc)
                if mi == (ma - 1) or mi == (ma - 2):
                    results.append("1")
                else:
                    results.append("2")
            elif b[1] == c[1]:
                mi = min(nb, nc)
                ma = max(nb, nc)
                if mi == (ma - 1) or mi == (ma - 2):
                    results.append("1")
                else:
                    results.append("2")
            else:
                results.append("2")
    # Aggregate output so total printed text scales linearly with n
    print("\n".join(results))


if __name__ == "__main__":
    main(10)