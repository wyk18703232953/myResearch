def main(n):
    # Interpret n as the number of different (l, r) test cases
    # Generate deterministic test cases based on n
    results = []
    for i in range(n):
        # Deterministic construction of l and r
        # l is even when i is even, odd when i is odd
        l = i * 2 + (i % 2)
        # Ensure r >= l and j = r - l + 1 varies with i
        r = l + (i % 5)  # j ranges from 1 to 5
        j = r - l + 1

        if j == 3:
            if l % 2 == 0:
                results.append((l, l + 1, l + 2))

            else:
                results.append(-1)
        elif j > 3:
            if l % 2 == 0:
                results.append((l, l + 1, l + 2))

            else:
                results.append((l + 1, l + 2, l + 3))

        else:
            results.append(-1)

    # Output results for inspection / complexity experiment
    for res in results:
        if res == -1:
            # print(-1)
            pass

        else:
            # print(res[0], res[1], res[2])
            pass
if __name__ == "__main__":
    main(10)