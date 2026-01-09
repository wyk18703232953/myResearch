def main(n):
    arr = []
    d = {}

    # Generate n deterministic expressions of the form "(a+b)/c"
    # Here a, b, c are derived deterministically from i
    for i in range(1, n + 1):
        a = i
        b = i + 1
        c = (i % 5) + 1  # c in [1..5], never zero
        s = f"({a}+{b})/{c}"

        a_parsed, b_parsed, c_parsed = tuple(
            map(
                int,
                s.replace("(", "").replace(")", "").replace("/", ".").replace("+", ".").split("."),
            )
        )
        x = (a_parsed + b_parsed) / c_parsed
        arr.append(x)
        if x not in d:
            d[x] = 0
        d[x] += 1

    for i in arr:
        # print(d[i], end=" ")
        pass
if __name__ == "__main__":
    main(10)