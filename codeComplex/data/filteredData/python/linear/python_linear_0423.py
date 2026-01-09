def main(n):
    # Deterministic generation of x and array a based on n
    x = (n * 37) ^ (n << 1)
    a = [((i * 17) ^ (i * i + n)) & ((1 << 20) - 1) for i in range(n)]

    s = set(a)
    if len(s) < n:
        # print(0)
        pass

    else:
        for i in a:
            if i & x != i and (i & x) in s:
                # print(1)
                pass
                break

        else:
            k = [i & x for i in a]
            if len(set(k)) < n:
                # print(2)
                pass

            else:
                # print(-1)
                pass
if __name__ == "__main__":
    main(10)