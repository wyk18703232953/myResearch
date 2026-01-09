def main(n):
    # Interpret n as the number of test cases
    t = n
    results = []
    for i in range(t):
        # Deterministically generate (a, b, d) based on i
        a = i
        b = i + 1
        d = 2 * i + 3

        if a > d or b > d:
            results.append(-1)
        elif a % 2 == b % 2:
            if a % 2 == d % 2:
                results.append(d)

            else:
                results.append(d - 2)

        else:
            if a % 2 == b % 2:
                if d % 2 == a % 2:
                    results.append(d)

                else:
                    results.append(d - 2)

            else:
                results.append(d - 1)

    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(10)