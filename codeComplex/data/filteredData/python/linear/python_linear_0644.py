def main(n):
    # Deterministic generation of input data
    # n is the size of the array a
    # Define a[i] = (i % 3) + 1 to ensure values >=1 and deterministic
    a = tuple((i % 3) + 1 for i in range(n))

    if n * 2 > sum(a) + 2:
        # print("NO")
        pass

    else:
        n1 = []
        on = []
        for i in range(n):
            if a[i] != 1:
                n1.append(i)

            else:
                on.append(i)
        # print("YES", len(n1) + min(2, len(on)) - 1)
        pass
        # print(n - 1)
        pass
        n1it = iter(n1)
        next(n1it)
        for v, u in zip(n1, n1it):
            # print(v + 1, u + 1)
            pass
        if on:
            # print(on.pop() + 1, n1[-1] + 1)
            pass
        if on:
            # print(on.pop() + 1, n1[0] + 1)
            pass
        on = iter(on)
        for n11 in n1:
            for i in range(a[n11] - 2):
                try:
                    # print(n11 + 1, next(on) + 1)
                    pass
                except StopIteration:
                    break

            else:
                continue
            break


if __name__ == "__main__":
    main(10)