def main(n):
    # Deterministically generate three strings resembling the original input pattern
    # Original logic expects strings like "1a", "2b" etc.
    # Use n to vary both digit and letter parts in a deterministic way
    a = f"{(n % 9) + 1}{chr(ord('a') + (n % 3))}"
    b = f"{(n % 9) + 1}{chr(ord('a') + ((n + 1) % 3))}"
    c = f"{((n + 1) % 9) + 1}{chr(ord('a') + ((n + 2) % 3))}"

    line = [a, b, c]
    line.sort()
    a, b, c = line

    if a == b and a == c:
        print(0)
    elif a == b:
        print(1)
    elif b == c:
        print(1)
    else:
        if (
            a[1] == b[1]
            and b[1] == c[1]
            and int(b[0]) - int(a[0]) == 1
            and int(c[0]) - int(b[0]) == 1
        ):
            print(0)
        elif a[1] == b[1] and int(b[0]) - int(a[0]) in [1, 2]:
            print(1)
        elif b[1] == c[1] and int(c[0]) - int(b[0]) in [1, 2]:
            print(1)
        elif a[1] == c[1] and int(c[0]) - int(a[0]) in [1, 2]:
            print(1)
        else:
            print(2)


if __name__ == "__main__":
    main(10)