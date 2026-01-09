def main(n):
    # Generate deterministic input data of size n
    # Original program expects:
    # n: number of integers
    # a: list of n integers
    # Here we generate a list where a[i] = i+1 to keep structure simple and deterministic.
    a = list(range(1, n + 1))
    a = sorted(a)
    s = []
    for q in a:
        for q1 in s:
            if q % q1 == 0:
                break

        else:
            s.append(q)
    # print(len(s))
    pass
if __name__ == "__main__":
    main(10)