def main(n):
    from math import ceil

    def solve():
        # Map n to problem parameters deterministically
        # Original input: n, a, b, c, t and array ti of length n
        nn = n
        a = 1 + (n % 5)
        b = 2 + (n % 7)
        c = 3 + (n % 11)
        t = n + a + b + c

        ti = [(i * 2 + (n % 3)) % (t + 1) for i in range(nn)]

        if b > c:
            # print(nn * a)
            pass

        else:
            ans = 0
            ti.sort()
            for x in ti:
                ans += (t - x) * (c - b) + a
            # print(ans)
            pass

    solve()


if __name__ == "__main__":
    main(10)