def main(n):
    # Generate a deterministic input list 'a' of length 14 based on n
    # Values grow roughly with n to let complexity scale with input magnitude
    a = [((i + 1) * (n + 1)) % 1000 for i in range(14)]

    mr = 0
    for t in range(14):
        b = list(a)
        m = b[t]
        k = t
        i = 1
        b[k] = 0
        while m > 0:
            if m // 14 == 0:
                b[(k + i) % 14] += 1
                m -= 1
                i += 1

            else:
                q = m // 14
                for c in range(14):
                    b[c] += q
                m -= 14 * q
        p = sum([x for x in b if x % 2 == 0])
        mr = max(p, mr)
    # print(mr)
    pass
if __name__ == "__main__":
    main(10)