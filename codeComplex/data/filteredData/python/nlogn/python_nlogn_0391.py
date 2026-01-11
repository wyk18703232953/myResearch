def main(n):
    # Map n to problem parameters:
    # Let k scale with n, and arrays a, b of length n
    if n <= 0:
        return

    k = max(0, n // 3)  # deterministic mapping from n to k

    # Deterministic construction of a, b
    # a: increasing-ish powers, b: counts with simple pattern
    a = [(i * 2 + 3) % (n + 7) for i in range(n)]
    b = [(i * i + 5) % (n + 11) for i in range(n)]

    c = list(sorted(zip(a, b, range(len(b)))))
    d = [0] * len(b)

    if k == 0:
        # print(' '.join(map(str, b)))
        pass

    else:
        best = [0] * k
        for pwr, cnt, index in c:
            d[index] = sum(best) + cnt

            if cnt > best[0]:
                for i in range(len(best)):
                    if cnt <= best[i]:
                        best.insert(i, cnt)
                        best = best[1:]
                        break

                else:
                    best = best[1:] + [cnt]

        # print(' '.join(map(str, d)))
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for experimentation
    main(10)