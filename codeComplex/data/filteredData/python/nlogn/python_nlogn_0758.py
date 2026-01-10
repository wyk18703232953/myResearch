def main(n):
    # Interpret n as the number of test cases
    t = n

    for case_idx in range(t):
        # For each test case, define the size of the array deterministically from case index
        size = case_idx + 3  # ensure size >= 3 so that ai[-2] is valid

        # Generate a deterministic array of integers based on case index
        # Example pattern: ai[j] = (case_idx + j) % (2*size) + 1
        ai = [(case_idx + j) % (2 * size) + 1 for j in range(size)]

        ai.sort()
        print(min(size - 2, ai[-2] - 1))


if __name__ == "__main__":
    main(5)