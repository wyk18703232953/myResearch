def main(n):
    # Deterministic generation of 'a' with exactly n digits.
    # For scalability and determinism, construct digits via simple arithmetic.
    # Ensure first digit is non-zero if n > 0.
    if n <= 0:
        a = 0

    else:
        digits = []
        for i in range(n):
            if i == 0:
                # Leading digit in [1..9] deterministically
                d = (i % 9) + 1

            else:
                d = (i % 10)
            digits.append(str(d))
        a = int("".join(digits))

    s = 0
    t = a
    b = []
    for _ in range(n):
        s += t % 10
        b.append(t % 10)
        t //= 10
    b.reverse()

    i = 2
    ans = False
    if s == 0:
        ans = True
    while i <= s:
        if s % i != 0:
            i += 1
            continue
        l = s // i
        c = 0
        su = 0
        for j in range(n):
            if su > l:
                break

            else:
                su += b[j]
                if su == l:
                    su = 0
                    c += 1
        if c == i:
            ans = True
        i += 1
    if ans:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)