def main(n):
    # Interpret n as the number of test cases
    T = n
    results = []

    for i in range(T):
        # Deterministically generate N based on i
        # Example scheme: cover both even and odd, various magnitudes
        N = (i + 1) * 2  # always even to exercise core logic; change if needed

        if N % 2 == 1:
            results.append("NO")

        else:
            N_half = N // 2
            if N_half ** (1 / 2) == int(N_half ** (1 / 2)):
                results.append("YES")

            else:
                if N_half % 2 == 1:
                    results.append("NO")

                else:
                    N_quarter = N_half // 2
                    if N_quarter ** (1 / 2) == int(N_quarter ** (1 / 2)):
                        results.append("YES")

                    else:
                        results.append("NO")

    # Output in the same format as original program
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    main(10)