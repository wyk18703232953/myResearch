n, m = 0, 0

def main(n_input):
    n = n_input
    m = n_input * (n_input + 1)

    out = [n]
    i = n - 1
    m -= 1
    for _ in range(n - 1):
        if m % 2:
            out.append(i)
        else:
            out = [i] + out
        m //= 2
        i -= 1

    for v in out:
        print(v, end=" ")
    print()


if __name__ == "__main__":
    main(10)