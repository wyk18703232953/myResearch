def main(n):
    # Deterministic generation of inputs based on n
    # Generate string a of digits '0'..'9' repeated deterministically
    a = [str((i * 7 + 3) % 10) for i in range(n)]
    # Generate upper bound b as a deterministic large integer depending on n
    # Ensure b has at least n digits to avoid trivial failures
    b_digits = [(i * 5 + 1) % 10 for i in range(max(1, n))]
    b_str = "".join(str(d) for d in b_digits).lstrip("0") or "0"
    b = int(b_str) + 10 ** max(1, n // 2)

    # Core algorithm from original code
    a.sort()
    a = a[::-1]
    prefix = ""
    while len(a) > 0:
        for i in range(len(a)):
            num = prefix + a[i] + "".join(sorted(a[:i] + a[i + 1:]))
            if int(num) <= b:
                prefix += a[i]
                a = a[:i] + a[i + 1:]
                break

        else:
            # If no digit can be appended without exceeding b, stop
            break

    # print(prefix)
    pass
if __name__ == "__main__":
    main(10)